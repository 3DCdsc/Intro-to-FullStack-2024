"""Setup sqlalchemy to use sqlite3 database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./my_db.db"


class Base(DeclarativeBase):
    """Base class for all data models.

    In SQLAlchemy, besides being used to track all data models, it also has properties
    that can customize SQLAlchemy's behavior. Most notably, the custom type mapping,
    see: <https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#customizing-the-type-map>.
    """

    def __repr__(self):
        """Allows User instances to be printed in a human-readable format."""
        return f"{self.__class__.__name__}({', '.join(f'{k}={getattr(self, k)!r}' for k in self.__table__.c.keys())})"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
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
