from db.database import engine
from db.tables import Base

Base.metadata.create_all(engine)
