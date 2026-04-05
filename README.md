# Crowd Funding Console App (Python)

A beginner-friendly Python console application for a simple crowd-funding workflow.

## Features

- User registration and login
- Email validation with regex
- Egyptian mobile number validation with regex
- Project creation with:
  - title
  - details
  - total target
  - start date
  - end date
- View all projects
- Edit only your own projects
- Delete only your own projects
- Search projects by date

## Tech Choices

- Python standard library only
- JSON file storage (no database)
- Modular code using small functions
- Automatic integer IDs for users and projects

## Project Structure

```text
crowd_funding_console_app/
├── main.py
├── auth.py
├── projects.py
├── storage.py
├── validators.py
├── utils.py
├── users.json
└── projects.json
```

## Menus

### Main menu

1. Register
2. Login
3. Exit

### User menu (after login)

1. Create project
2. View all projects
3. Edit my project
4. Delete my project
5. Search projects by date
6. Logout

## Run the App

```bash
python main.py
```

If your system uses `py` launcher:

```bash
py main.py
```

## Data Files

- `users.json`: stores users
- `projects.json`: stores projects

Both files are automatically created/used by the app.

## Notes

- Passwords are stored as plain text to match lab requirements.
- Dates must be in `YYYY-MM-DD` format.
- Start date must be before end date.
