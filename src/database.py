import sqlite3
import os
from datetime import datetime
from src.logger import logger

# ✅ Define base path safely (works locally & in Docker)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  # ✅ ensure folder exists

# ✅ Database path (automatically created if missing)
DB_PATH = os.path.join(DATA_DIR, "water_data.db")


def init_db():
    """Create the intake table if not already existing."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS intake(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                date TEXT NOT NULL,
                intake_ml INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Error initializing database: {e}")


def log_intake(user_id: str, intake_ml: int):
    """Insert a new water intake record."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO intake (user_id, date, intake_ml) VALUES (?, ?, ?)",
            (user_id, date, intake_ml)
        )
        conn.commit()
        conn.close()
        logger.info(f"💧 Logged {intake_ml} ml for {user_id}")
    except Exception as e:
        logger.error(f"❌ Error logging intake: {e}")


def intake_history(user_id: str):
    """Fetch the intake history for a given user."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM intake WHERE user_id = ? ORDER BY date DESC",
            (user_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        logger.info(f"📜 Retrieved {len(rows)} records for {user_id}")
        return rows
    except Exception as e:
        logger.error(f"❌ Error fetching history: {e}")
        return []


# ✅ Run once if executed directly (not when imported)
if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
