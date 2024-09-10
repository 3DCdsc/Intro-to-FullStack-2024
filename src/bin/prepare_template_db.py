#!/usr/bin/env python3

import sys
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    from src import Base

    engine = create_engine("sqlite:///src/template.db")

    Session = sessionmaker(bind=engine)

    with Session.begin() as sess:
        Base.metadata.create_all(sess.bind)

    # TODO: The rest of the example data setup.


if __name__ == "__main__":
    # Tomfoolery to allow importing src although its not a proper package.
    sys.path.append(str((Path(__file__) / ".." / ".." / "..").resolve()))
    main()
