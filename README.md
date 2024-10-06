# Intro-to-FullStack-2024

A 3? part workshop series on fullstack development. Each part will be in its own branch.

## Prerequisites

- Git (<https://git-scm.com/downloads>)
  - Please install Git Bash

## Install

```sh
python -m venv venv
# Git Bash for Windows
source venv\Scripts\activate
# MacOS
source venv\bin\activate
pip install -r requirements.txt
```

## Note

- We will be using SQLAlchemy 2.0. The library's API is quite different, but I think
  its better to avoid teaching outdated things and this provides value to those who
  may have used SQLAlchemy before.
- Because of table structure, process of normalization. If you find it hard to normalize
  that means structured documents probably better. Many-to-many needs association tables.
- <https://pypi.org/project/SQLAlchemy-Utc/>
- Diagram of what an operation should do shown side by side during workshop so they can implement it themselves.
