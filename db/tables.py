from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

Base = declarative_base()


class Tokens(Base):
    __tablename__ = 'tokens'

    token = sa.Column(sa.VARCHAR, primary_key=True)
