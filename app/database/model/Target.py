from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.settings.psql_config import Base

class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    target_type_id = Column(Integer, ForeignKey("targettype.target_type_id"))
    target_priority = Column(String)