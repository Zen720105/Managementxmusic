import sqlite3
from typing import List

# Establish connection to the database
conn = sqlite3.connect("VIPMUSIC.db", check_same_thread=False)
cursor = conn.cursor()

# Create the locks table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS locks (
    chat_id INTEGER NOT NULL,
    lock_type TEXT NOT NULL,
    PRIMARY KEY (chat_id, lock_type)
)
""")
conn.commit()

def add_lock(chat_id: int, lock_type: str):
    """
    Adds a lock to the specified chat.
    """
    cursor.execute("INSERT OR IGNORE INTO locks (chat_id, lock_type) VALUES (?, ?)", (chat_id, lock_type))
    conn.commit()

def remove_lock(chat_id: int, lock_type: str):
    """
    Removes a lock from the specified chat.
    """
    cursor.execute("DELETE FROM locks WHERE chat_id = ? AND lock_type = ?", (chat_id, lock_type))
    conn.commit()

def is_locked(chat_id: int, lock_type: str) -> bool:
    """
    Checks if a specific lock is applied in a chat.
    """
    cursor.execute("SELECT 1 FROM locks WHERE chat_id = ? AND lock_type = ? LIMIT 1", (chat_id, lock_type))
    return cursor.fetchone() is not None

def get_locks(chat_id: int) -> List[str]:
    """
    Retrieves all lock types applied in a specific chat.
    """
    cursor.execute("SELECT lock_type FROM locks WHERE chat_id = ?", (chat_id,))
    return [row[0] for row in cursor.fetchall()]
