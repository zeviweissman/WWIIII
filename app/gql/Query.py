from app.gql.types import MissionType, MissonLimtedType, CityStatsType
from graphene import ObjectType, List, String, Field, Int
import app.database.repository.mission_repository as mission_repos
import app.service.mission_service as mission_service
from sqlalchemy import Date


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int())
    missions_by_date = List(MissionType, mission_date=String())
    missions_by_country = List(MissionType, country=String())
    missions_by_target_industry = List(MissionType, industry=String())
    mission_results_by_target_type = List(MissonLimtedType, target_type=String())
    missions_stats_by_city = Field(CityStatsType, city=String())


    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return (mission_repos.get_mission_by_id(mission_id)
                .value_or(f"couldnt find mission by id {mission_id}"))


    @staticmethod
    def resolve_missions_by_date(root, info, mission_date):
        return mission_repos.get_mission_by_date(mission_date)


    @staticmethod
    def resolve_missions_by_country(root, info, country):
        return mission_repos.get_mission_by_country(country)

    @staticmethod
    def resolve_missions_by_target_industry(root, info, industry):
        return mission_repos.get_mission_by_target_industry(industry)

    @staticmethod
    def resolve_mission_results_by_target_type(root, info, target_type):
        return mission_repos.get_mission_results_by_target_type(target_type)

    @staticmethod
    def resolve_missions_stats_by_city(root, info, city):
        info = mission_service.get_mission_stats_by_city(city)
        return CityStatsType(**info)