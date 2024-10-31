from graphene_sqlalchemy import SQLAlchemyObjectType
from app.database.model import Mission

class MissionType(SQLAlchemyObjectType):
    class Meta:
        model = Mission