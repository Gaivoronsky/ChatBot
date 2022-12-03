from transformers import AutoTokenizer, AutoModelForCausalLM
from telethon import TelegramClient, events, sync
import torch
import time

from settings import settings
from db.db import ClassDB


class ManagementTG:
    def __init__(self, interval_check: int = 1, model_name: str = "inkoziev/rugpt_chitchat", is_docker: bool = True):
        self.client = TelegramClient('session', settings.api_id, settings.api_hash)
        self.client.connect()
        self.interval_check = interval_check
        self.db = ClassDB()
        self.token = None

        if not self.client.is_user_authorized():
            if is_docker:
                self.client.send_code_request(settings.phone)
                while not self.token:
                    token = self.db.get_token()
                    time.sleep(2)
                    if token:
                        self.token = token.token
                        self.db.delete_token()
                        self.client.sign_in(settings.phone, self.token)
            else:
                self.client.send_code_request(settings.phone)
                self.client.sign_in(settings.phone, input('Enter the code: '))

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.add_special_tokens({'bos_token': '<s>', 'eos_token': '</s>', 'pad_token': '<pad>'})
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

        self.history_messages = set(self.get_message())
        self.max_len_history = 10
        self.start_len_history = 3

    def send_message(self, text: str = 'Гы', chat_id: int = settings.chat_id):
        self.client.send_message(chat_id, text, parse_mode='html')

    def create_answer(self, chat_id: int = settings.chat_id, len_history: int = 1):
        history_message = '<s>' + '\n'.join(
            [f'- {i}' for i in
             self.get_message(chat_id, count=min(len_history, self.max_len_history), all_message=True)][::-1]
        ) + '\n-'
        encoded_prompt = self.tokenizer.encode(
            history_message,
            add_special_tokens=False,
            return_tensors="pt"
        ).to(self.device)

        output_sequences = self.model.generate(
            input_ids=encoded_prompt,
            max_length=100,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.pad_token_id
        )

        text = self.tokenizer.decode(output_sequences[0].tolist(), clean_up_tokenization_spaces=True)[
               len(history_message) + 1:]
        text = text[: text.find('</s>')]
        return text[: text.find('-')]

    def get_message(self, chat_id: int = settings.chat_id, count: int = 10, all_message: bool = False) -> list:
        history = []
        for i, message in enumerate(self.client.iter_messages(chat_id)):
            if i > count:
                break
            if all_message:
                history.append(message.message)
            else:
                if not message.from_id:
                    history.append(message.message)

        return history

    def new_message(self, chat_id: int = settings.chat_id) -> list:
        messages = set(self.get_message(chat_id))
        new = messages - self.history_messages

        if new:
            self.history_messages.update(new)
            return list(new)

    def loop(self, chat_id: int = settings.chat_id):
        print('START')
        counter = self.start_len_history

        my_message = self.create_answer(chat_id, len_history=counter)
        self.send_message(my_message)
        counter += 1

        while True:
            messages = self.new_message()
            if messages:
                my_message = self.create_answer(chat_id, len_history=counter)
                self.send_message(my_message)
                counter += 1
            time.sleep(self.interval_check)


if __name__ == '__main__':
    tg = ManagementTG()

