from graphene_sqlalchemy import SQLAlchemyObjectType
from app.database.model import City

class CityType(SQLAlchemyObjectType):
    class Meta:
        model = City