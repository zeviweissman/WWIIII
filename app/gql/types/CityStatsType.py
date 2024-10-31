from graphene import ObjectType, Int, Float


class CityStatsType(ObjectType):
    mission_count = Int()
    avg_priority_points = Float()