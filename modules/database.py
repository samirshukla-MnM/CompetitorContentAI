from sqlalchemy import create_engine,text
from config import DB_PATH

engine=create_engine(f"sqlite:///{DB_PATH}")

def init_db():
    with engine.begin() as conn:
        conn.execute(text('''
        CREATE TABLE IF NOT EXISTS urls(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_name TEXT,
            our_url TEXT,
            competitor1 TEXT,
            competitor2 TEXT,
            competitor3 TEXT
        );
        '''))
