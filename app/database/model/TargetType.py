from sqlalchemy import Column, Integer, String
from app.settings.psql_config import Base

class TargetType(Base):
    __tablename__ = "targettypes"
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String)
