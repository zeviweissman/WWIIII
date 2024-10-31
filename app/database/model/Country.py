from sqlalchemy import Column, Integer, String
from app.settings.psql_config import Base
from sqlalchemy.orm import relationship


class Country(Base):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)

    cities = relationship("City", back_populates="country")
