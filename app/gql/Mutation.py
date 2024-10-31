from app.gql.mutations import AddMission, AddTarget, EditMission, DeleteMission
from graphene import ObjectType

class Mutation(ObjectType):
    AddMission = AddMission.Field()
    AddTarget = AddTarget.Field()
    EditMission = EditMission.Field()
    DeleteMission = DeleteMission.Field()