from app.database.connection.psql import get_session
from app.gql.inputs import MissionUpdateInput
from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from app.database.model import Mission, Country, Target, City, TargetType
from sqlalchemy import Date
from sqlalchemy.exc import SQLAlchemyError
from typing import List




def get_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with get_session() as session:
        return (Maybe.from_optional(
            session.get(Mission, mission_id)
        ))


def get_mission_by_date(mission_date: Date) -> List[Mission]:
    with get_session() as session:
        return (session.query(Mission)
                .filter_by(mission_date=mission_date)
                .all())


def get_mission_by_country(country: str) -> List[Mission]:
    with get_session() as session:
        return (session.query(Mission)
                .join(Target)
                .join(City)
                .join(Country)
                .filter(Country.country_name == country)
                .all())


def get_mission_by_target_industry(target_industry: str) -> List[Mission]:
    with get_session() as session:
        return (session.query(Mission)
                .join(Target)
                .filter(Target.target_industry == target_industry)
                .all())


def get_mission_results_by_target_type(target_type: str):
    with get_session() as session:
        return (session.query(Mission)
                .join(Target)
                .join(TargetType)
                .filter(TargetType.target_type_name == target_type)
                .all()
        )


def insert_mission(mission: Mission) -> Result[Mission, str]:
    with get_session() as session:
        try:
            max_id = session.query(Mission).order_by(Mission.mission_id.desc()).first().mission_id
            mission.mission_id = max_id + 1
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))



def update_mission(mission_input: MissionUpdateInput) -> Result[Mission, str]:
    with get_session() as session:
        try:
            mission_to_update = session.get(Mission, mission_input.mission_id)
            if mission_input.aircraft_returned:
                mission_to_update.aircraft_returned = mission_input.aircraft_returned
            if mission_input.aircraft_failed:
                mission_to_update.aircraft_failed = mission_input.aircraft_failed
            if mission_input.aircraft_damaged:
                mission_to_update.aircraft_damaged = mission_input.aircraft_damaged
            if mission_input.aircraft_lost:
                mission_to_update.aircraft_lost = mission_input.aircraft_lost
            session.commit()
            session.refresh(mission_to_update)
            return Success(mission_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def delete_mission_by_id(mission_id):
    with get_session() as session:
        try:
            mission_to_delete = session.get(Mission, mission_id)
            session.delete(mission_to_delete)
            session.commit()
            return Success(mission_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))