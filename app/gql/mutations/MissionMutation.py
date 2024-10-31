from app.database.model import Mission
import app.database.repository.mission_repository as mission_repos
from app.gql.types import MissionType
from graphene import String, Mutation, Field, Boolean, Int
from app.gql.inputs import MissionUpdateInput, MissionInsertInput



class AddMission(Mutation):
   class Arguments():
      mission_input = MissionInsertInput()
   mission = Field(MissionType, default_value=None)
   success = Field(Boolean, default_value=True)

   @staticmethod
   def mutate(root, info, mission_input: MissionInsertInput):
      mission = (mission_repos.insert_mission(Mission(**mission_input))
                 .value_or(None))
      return AddMission(mission=mission) if mission else AddMission(success=False)



class EditMission(Mutation):
   class Arguments():
      mission_input = MissionUpdateInput()
   mission = Field(MissionType, default_value=None)
   success = Field(Boolean, default_value=True)

   @staticmethod
   def mutate(root, info, mission_input: MissionUpdateInput):
      mission = (mission_repos.update_mission(mission_input)
                 .value_or(None))
      return EditMission(mission=mission) if mission else EditMission(success=False)