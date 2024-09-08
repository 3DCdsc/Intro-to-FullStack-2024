"""Setup sqlalchemy to use sqlite3 database.

Referenced from <https://fastapi.tiangolo.com/tutorial/sql-databases>.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./my_db.db"


class Base(DeclarativeBase):
    pass


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # Print out all the sql commands used; not sure if useful for workshop?
    # connect_args={"check_same_thread": False},  # Only useful with FastAPI in part 2.
)

# See: https://docs.sqlalchemy.org/en/20/orm/session_api.html
# A factory for pre-configured Session objects to avoid the need to use engine directly.
Session = sessionmaker(
    bind=engine,
    # FastAPI handles these.
    autocommit=False,
    autoflush=False,
)
