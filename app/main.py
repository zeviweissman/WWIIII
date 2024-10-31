from app.database.model import *
from app.database.connection.psql import get_session, initate_db




if __name__ == "__main__":
    with get_session() as session:
        a = session.query(City).all()
        print(a)