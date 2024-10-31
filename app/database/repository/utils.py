from app.database.model import Mission
from app.gql.inputs import MissionUpdateInput


def mission_model_for_update(mission_to_update: Mission, mission_input: MissionUpdateInput) -> Mission:
    if mission_input.aircraft_returned:
        mission_to_update.aircraft_returned = mission_input.aircraft_returned
    if mission_input.aircraft_failed:
        mission_to_update.aircraft_failed = mission_input.aircraft_failed
    if mission_input.aircraft_damaged:
        mission_to_update.aircraft_damaged = mission_input.aircraft_damaged
    if mission_input.aircraft_lost:
        mission_to_update.aircraft_lost = mission_input.aircraft_lost
