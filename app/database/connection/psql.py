from app.settings.psql_config import engine, _session_factory, Base


def get_session():
    return _session_factory()



