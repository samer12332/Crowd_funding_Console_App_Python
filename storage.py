import json
import os

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"


def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file)
        except Exception as error:
            print(f"Error creating {file_path}: {error}")


def load_data(file_path):
    ensure_file_exists(file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    except Exception as error:
        print(f"Error loading {file_path}: {error}")
        return []


def save_data(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except Exception as error:
        print(f"Error saving {file_path}: {error}")


def load_users():
    return load_data(USERS_FILE)


def save_users(users):
    save_data(USERS_FILE, users)


def load_projects():
    return load_data(PROJECTS_FILE)


def save_projects(projects):
    save_data(PROJECTS_FILE, projects)
