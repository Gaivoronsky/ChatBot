from db.database import Session
from db.tables import Tokens


class ClassDB:
    def __init__(self, session: Session = Session()):
        self.session = session

    def add_token(self, token):
        tokens_table = Tokens(
            token=token,
        )
        self.session.add(tokens_table)
        self.session.commit()

    def get_token(self):
        query = self.session.query(Tokens).first()
        return query

    def delete_token(self):
        operation = self.get_token()
        self.session.delete(operation)
        self.session.commit()
