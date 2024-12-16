import sqlite3
from my_exceptions import DatabaseError


DATABASE = "pynative.db"

class Database:
    """Database Connection Manager"""
    def __init__(self, db_file):
        self.db_file = DATABASE

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()

    def execute(self, query, params=()):
        """Execute a query with parameters"""
        print("query", query)
        print("params", params)
        try:
            self.cursor.execute(query, params)
        except sqlite3.OperationalError as exc:
            raise DatabaseError(f"Database Operational Error: {exc}")
        except sqlite3.Error as exc:
            raise DatabaseError(f"Database Connection Error: {exc}")
        return self.cursor

