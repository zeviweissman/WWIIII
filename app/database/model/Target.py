from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.settings.psql_config import Base
from sqlalchemy.orm import relationship


class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    target_type_id = Column(Integer, ForeignKey("targettypes.target_type_id"))
    target_priority = Column(Integer)


    target_type = relationship("TargetType", back_populates="target", lazy='joined')
    city = relationship("City", back_populates="targets", lazy="joined")
    mission = relationship("Mission", back_populates="target")