from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.settings.psql_config import Base
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey("contries.country_id"))
    latitude = Column(Float)
    longitude = Column(Float)
