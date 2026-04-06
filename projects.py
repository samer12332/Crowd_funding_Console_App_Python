from datetime import datetime
from storage import load_projects, save_projects
from validators import parse_valid_date
from utils import get_next_id


def create_project(logged_in_user):
    projects = load_projects()

    title = input("Project title: ").strip()
    if not title:
        print("Title is required.")
        return

    details = input("Project details: ").strip()
    total_target_str = input("Total target: ").strip()
    try:
        total_target = float(total_target_str)
        if total_target <= 0:
            print("Total target must be greater than 0.")
            return
    except ValueError:
        print("Total target must be a number.")
        return

    start_date_str = input("Start date (YYYY-MM-DD): ").strip()
    end_date_str = input("End date (YYYY-MM-DD): ").strip()

    start_date = parse_valid_date(start_date_str)
    end_date = parse_valid_date(end_date_str)

    if not start_date or not end_date:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    if start_date.date() <= datetime.today().date():
        print("Start date must be a future date.")
        return

    if start_date >= end_date:
        print("Start date must be before end date.")
        return

    new_project = {
        "project_id": get_next_id(projects, "project_id"),
        "owner_user_id": logged_in_user["user_id"],
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date_str,
        "end_date": end_date_str,
    }

    projects.append(new_project)
    save_projects(projects)
    print("Project created successfully.")


def view_all_projects():
    projects = load_projects()

    if not projects:
        print("No projects found.")
        return

    print("\n=== All Projects ===")
    for project in projects:
        print(f"Project ID: {project.get('project_id')}")
        print(f"Owner User ID: {project.get('owner_user_id')}")
        print(f"Title: {project.get('title')}")
        print(f"Details: {project.get('details')}")
        print(f"Total Target: {project.get('total_target')}")
        print(f"Start Date: {project.get('start_date')}")
        print(f"End Date: {project.get('end_date')}")
        print("-" * 30)


def edit_my_project(logged_in_user):
    projects = load_projects()

    try:
        project_id = int(input("Enter your project ID to edit: ").strip())
    except ValueError:
        print("Project ID must be an integer.")
        return
    except Exception as error:
        print(f"Input error: {error}")
        return

    project = find_project_by_id(projects, project_id)
    if not project:
        print("Project not found.")
        return

    if project.get("owner_user_id") != logged_in_user.get("user_id"):
        print("You can only edit your own projects.")
        return

    
    new_title = input(f"New title [{project.get('title')}]: ").strip()
    new_details = input(f"New details [{project.get('details')}]: ").strip()
    new_total_target_str = input(f"New total target [{project.get('total_target')}]: ").strip()
    new_start_date_str = input(f"New start date [{project.get('start_date')}] (YYYY-MM-DD): ").strip()
    new_end_date_str = input(f"New end date [{project.get('end_date')}] (YYYY-MM-DD): ").strip()
    

    updated_title = new_title if new_title else project.get("title")
    updated_details = new_details if new_details else project.get("details")

    if new_total_target_str:
        try:
            updated_total_target = float(new_total_target_str)
            if updated_total_target <= 0:
                print("Total target must be greater than 0.")
                return
        except ValueError:
            print("Total target must be a number.")
            return
    else:
        updated_total_target = project.get("total_target")

    updated_start_date_str = new_start_date_str if new_start_date_str else project.get("start_date")
    updated_end_date_str = new_end_date_str if new_end_date_str else project.get("end_date")

    updated_start_date = parse_valid_date(updated_start_date_str)
    updated_end_date = parse_valid_date(updated_end_date_str)

    if not updated_start_date or not updated_end_date:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    if updated_start_date >= updated_end_date:
        print("Start date must be before end date.")
        return

    project["title"] = updated_title
    project["details"] = updated_details
    project["total_target"] = updated_total_target
    project["start_date"] = updated_start_date_str
    project["end_date"] = updated_end_date_str

    save_projects(projects)
    print("Project updated successfully.")


def delete_my_project(logged_in_user):
    projects = load_projects()

    try:
        project_id = int(input("Enter your project ID to delete: ").strip())
    except ValueError:
        print("Project ID must be an integer.")
        return

    project = find_project_by_id(projects, project_id)
    if not project:
        print("Project not found.")
        return

    if project.get("owner_user_id") != logged_in_user.get("user_id"):
        print("You can only delete your own projects.")
        return

    projects.remove(project)
    save_projects(projects)
    print("Project deleted successfully.")


def search_projects_by_date():
    projects = load_projects()

    if not projects:
        print("No projects found.")
        return


    search_date_str = input("Enter date to search (YYYY-MM-DD): ").strip()

    search_date = parse_valid_date(search_date_str)
    if not search_date:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    matched_projects = []
    for project in projects:
        start_date = parse_valid_date(project.get("start_date", ""))
        end_date = parse_valid_date(project.get("end_date", ""))

        if start_date and end_date and start_date <= search_date <= end_date:
            matched_projects.append(project)

    if not matched_projects:
        print("No projects found for this date.")
        return

    print("\n=== Matching Projects ===")
    for project in matched_projects:
        print(f"Project ID: {project.get('project_id')} | Title: {project.get('title')} | Owner User ID: {project.get('owner_user_id')}")


def find_project_by_id(projects, project_id):
    for project in projects:
        if project.get("project_id") == project_id:
            return project
    return None

