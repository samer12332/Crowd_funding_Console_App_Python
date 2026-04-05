import auth
import projects


def main_menu():
    while True:
        print("\n=== Crowd-Funding App ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                auth.register_user()
            case "2":
                user = auth.login_user()
                if user:
                    user_menu(user)
            case "3":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


def user_menu(logged_in_user):
    while True:
        print(f"\n=== Welcome, {logged_in_user['first_name']} ===")
        print("1. Create project")
        print("2. View all projects")
        print("3. Edit my project")
        print("4. Delete my project")
        print("5. Search projects by date")
        print("6. Logout")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                projects.create_project(logged_in_user)
            case "2":
                projects.view_all_projects()
            case "3":
                projects.edit_my_project(logged_in_user)
            case "4":
                projects.delete_my_project(logged_in_user)
            case "5":
                projects.search_projects_by_date()
            case "6":
                print("Logged out.")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
