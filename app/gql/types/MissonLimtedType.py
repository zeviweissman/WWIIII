from graphene import ObjectType, Float


class MissonLimtedType(ObjectType):
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()