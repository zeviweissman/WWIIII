from sqlalchemy import Column, Integer, String
from app.settings.psql_config import Base
from sqlalchemy.orm import relationship


class TargetType(Base):
    __tablename__ = "targettypes"
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)

    target = relationship("Target", back_populates="target_type")
