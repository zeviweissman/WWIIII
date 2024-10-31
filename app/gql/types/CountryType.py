from graphene_sqlalchemy import SQLAlchemyObjectType
from app.database.model import Country

class CountryType(SQLAlchemyObjectType):
    class Meta:
        model = Country