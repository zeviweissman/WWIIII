from app.database.model import Target
from returns.result import Result


def insert_target(target: Target) -> Result[Target, str]:
    with get_session() as session:
        try:
            max_id = session.query(Target).order_by(Target.target_id.desc()).first().target_id
            target.target_id = max_id + 1
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))