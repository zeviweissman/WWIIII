from graphene_sqlalchemy import SQLAlchemyObjectType
from app.database.model import TargetType

class TargetTypeType(SQLAlchemyObjectType):
    class Meta:
        model = TargetType