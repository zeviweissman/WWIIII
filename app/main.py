from app.database.model import *
from app.database.connection.psql import get_session




if __name__ == "__main__":
    with get_session() as session:
        a = session.query(Mission).all()
        print(a)