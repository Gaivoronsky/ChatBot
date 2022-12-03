## Description

This bot works only in Russian.
It is based on neural network transformer models.
It now supports a conversation context of up to 10 messages.

## Project structure

```
├── .git                  <- Git (read-only)
├── api                   <- API code
├── bot                   <- ChatBot code
├── docker-compose.yml    <- Make file project
├── pyproject.toml        <- File for poetry
├── README.md             <- It's me
```

## Install Docker

- Install [Docker](https://docs.docker.com/desktop/install/windows-install/) and [WSL 2 backend](https://learn.microsoft.com/ru-ru/windows/wsl/install)
- Create [API ID and API HASH](https://core.telegram.org/api/obtaining_api_id)
- Start Docker
- Find id people for chat and your id. For it uses [tg bot](https://t.me/username_to_id_bot)
- Create .env file by path bot/.env
```bash
API_ID="API_ID"
API_HASH="API_HASH"
PHONE="PHONE"
MY_ID=MY_ID
CHAT_ID=CHAT_ID
```  
- Execute command
```bash
docker-compose up -d --build
```
- Open website in browser [localhost](http://localhost)
- Input telegram key in field
- All Done!
- For stop ChatBot uses next command
```bash
docker-compose down
```

## Install local 

- Go to directory
```bash
cd bot
```
- Installing dependencies:
```bash
poetry install
poetry shell
```
- Create .env file by path bot/.env
```bash
API_ID="API_ID"
API_HASH="API_HASH"
PHONE="PHONE"
MY_ID=MY_ID
CHAT_ID=CHAT_ID
```  
- Start API:
```bash
python -m core
```