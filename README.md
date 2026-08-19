# Python based bike database (SQLite) reader

> **Archived.** Python practice project from 2023, written while learning.
> Not maintained.

## This project was created for University of Helsinki: Basics of databases course, and it's further developed by me.

## Installation: 

1. Search information how to install Python3 and SQLite on your system.
2. Download the source code
3. Run the main file (main.py) with Python3

## Database

`bikes.db` is **not included** in this repository — it is a 37 MB SQLite file and was
removed from version control to keep the repo small. `bikes.py` expects to find it in
the project root:

```python
db = sqlite3.connect('bikes.db')
```

Supply your own `bikes.db` with the same schema to run the reader.
