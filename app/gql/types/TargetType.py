from graphene_sqlalchemy import SQLAlchemyObjectType
from app.database.model import Target

class TargetType(SQLAlchemyObjectType):
    class Meta:
        model = Target