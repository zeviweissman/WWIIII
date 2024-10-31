from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_repr import RepresentableBase

DB_URL = 'postgresql://admin:1234@172.23.43.73:5432/missions_db'
Base = declarative_base(cls=RepresentableBase)
engine = create_engine(DB_URL)
_session_factory = sessionmaker(bind=engine)