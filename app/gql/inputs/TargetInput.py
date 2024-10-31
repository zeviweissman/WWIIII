from graphene import InputObjectType, Int, String


class TargetInput(InputObjectType):
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = String()