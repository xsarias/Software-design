"""
This is the main file of the project. It is the entry point of the application.

Author: Xiomara Arias <xsariasa@udistrital.edu.co>
"""

from .core_subsystem import FinalCatalog, Authentication

CATALOG = FinalCatalog()

# Messages for login and menu options
LOGIN_LETTER = """
>>> WELCOME TO VEHICLE CATALOG SYSTEM <<<
1). Log in.
2). Sign up.
3). Exit.
"""

MENU_OPTIONS = """
1. Search all vehicles
2. Search vehicles by speed
3. Search vehicles by price
"""

MENU_USER = """
4. Subscribe to newsletter.
"""

MENU_ADMIN = """
4. Add a new vehicle
5. Remove a vehicle
6. Send newsletter.
"""

def login():
    """This function allows the user to log in the system."""
    username = input("->Username: ")
    password = input("->Password: ")

    auth = Authentication(username, password)

    if auth.authenticate():
        return auth.userdata()
    return None

def register():
    """This function allows the user to register a new account."""
    username = input("->Enter new username: ")
    password = input("->Enter new password: ")
    auth = Authentication(username, password)
    
    # While user exists, prompt for new registration
    while auth.authenticate():
        print("The user already exists, please provide different data.")
        username = input("->Enter new username: ")
        password = input("->Enter new password: ")
        auth = Authentication(username, password)

    op = int(input("Select a user type: (1) Admin or (2) User: "))
    grants = False
    if op == 1:
        grants = True

    auth = Authentication(username, password)
    auth.register(grants)
    
    # Check if registration was successful and return user data
    if auth.authenticate():
        print(f"User {username} registered successfully!")
        return auth.userdata()
    return None

def main():
    """This is the main file of the project."""
    user = None
    print(LOGIN_LETTER)

    while True:
        option = int(input("Please select an option: "))
        if option == 1:
            print(">>>>>>--- LOG IN ---<<<<<<")
            user = login()
            # While user is None, prompt for new authentication
            while user == None:
                print("The username or password is incorrect, please try again.")
                user = login()
            break
        elif option == 2:
            print(">>>>>>--- SIGN UP ---<<<<<<")
            print("Welcome to Vehicle constructor, please provide the following information to register you.")
            user = register()
            break
        elif option == 3:
            print("Exiting the system. Goodbye!")
            return  # Exit program if option is 3

    print(MENU_OPTIONS)
    if user.is_grant(True):
        print(MENU_ADMIN)
        option = input("Please select an option: ")

        if option == "1":
            print("====== Searching all vehicles ======")
            CATALOG.get_all_vehicles()
        elif option == "2":
            print("====== Searching vehicles by speed ======")
            CATALOG.get_vehicles_by_speed()
        elif option == "3":
            print("====== Searching vehicles by price ======")
            CATALOG.get_vehicles_by_price()
        elif option == "4":
            print("====== Adding a new vehicle ======")
            CATALOG.add_vehicle(user.get_username())
        elif option == "5":
            print("====== Removing a vehicle ======")
            CATALOG.remove_vehicle()
        elif option == "6":
            print("====== Sending newsletter ======")
            # Implement the logic to send newsletter here
        else:
            print("Invalid option. Please select a valid option.")
    else:
        print(MENU_USER)
        option = input("Please select an option: ")
        if option == "1":
            print("====== Searching all vehicles ======")
            CATALOG.get_all_vehicles()
        elif option == "2":
            print("====== Searching vehicles by speed ======")
            CATALOG.get_vehicles_by_speed()
        elif option == "3":
            print("====== Searching vehicles by price ======")
            CATALOG.get_vehicles_by_price()
        elif option == "4":
            print("====== Subscribe to newsletter ======")
            CATALOG.get_vehicles_by_price()

if __name__ == "__main__":
    main()
