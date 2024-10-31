from app.database.model import Target
import app.database.repository.target_repository as target_repos
from app.gql.types import TargetType
from graphene import String, Mutation, Field, Boolean
from app.gql.inputs import TargetInput



class AddTarget(Mutation):
   class Arguments():
      target_input = TargetInput()
   target = Field(TargetType, default_value=None)
   success = Field(Boolean, default_value=True)

   @staticmethod
   def mutate(root, info, target_input: TargetInput):
      target = (target_repos.insert_target(Target(**target_input))
                 .value_or(None))
      return AddTarget(target=target) if target else AddTarget(success=False)