# database.py
from typing import Dict, List

# Simulating a database with a dictionary
LOCKS_DB: Dict[int, List[str]] = {}

async def add_lock(chat_id: int, lock_type: str):
    """Add a lock to a specific chat."""
    if chat_id not in LOCKS_DB:
        LOCKS_DB[chat_id] = []
    if lock_type not in LOCKS_DB[chat_id]:
        LOCKS_DB[chat_id].append(lock_type)

async def remove_lock(chat_id: int, lock_type: str):
    """Remove a lock from a specific chat."""
    if chat_id in LOCKS_DB and lock_type in LOCKS_DB[chat_id]:
        LOCKS_DB[chat_id].remove(lock_type)

async def is_locked(chat_id: int, lock_type: str) -> bool:
    """Check if a specific type of content is locked in a chat."""
    return chat_id in LOCKS_DB and lock_type in LOCKS_DB[chat_id]
