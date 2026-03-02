import os
import json
from typing import List, TypedDict
from config import DB_PATH


class User(TypedDict):
    id: int
    name: str
    email: str
    password: str
    balance: float


def read_json() -> List[User]:
    """Read the JSON file and return the data"""
    try:
        with open(DB_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_json(data: List[User]) -> None:
    """Write the data to the JSON file"""
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def initialize_json() -> None:
    """Initialize the JSON file if it doesn't exist. Creates parent dir if needed."""
    if not os.path.isfile(DB_PATH):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        write_json([])


def add_user(user: User) -> bool:
    """Add a user to the JSON file and return True if successful, False otherwise"""
    users = read_json()

    if any(u["id"] == user["id"] for u in users):
        return False

    users.append(user)
    write_json(users)
    return True

def get_user_by_id(user_id: int) -> User | None:
    """Get a user from the JSON file and return it if found, otherwise return None"""
    users = read_json()
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def get_user_by_email(email: str) -> User | None:
    """Get a user from the JSON file and return it if found, otherwise return None"""
    users = read_json()
    for user in users:
        if user["email"] == email:
            return user
    return None

def update_user(user_id: int, updates: dict) -> bool:
    """Update a user in the JSON file and return True if successful, False otherwise"""
    users = read_json()

    for user in users:
        if user["id"] == user_id:
            user.update(updates)
            write_json(users)
            return True

    return False

def delete_user(user_id: int) -> bool:
    """Delete a user from the JSON file and return True if successful, False otherwise"""
    users = read_json()
    new_users = [u for u in users if u["id"] != user_id]

    if len(new_users) == len(users):
        return False

    write_json(new_users)
    return True