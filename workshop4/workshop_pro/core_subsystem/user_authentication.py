"""
This module has some classes related to users and authentication.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

import json
import os

class User:
    """This is a data class to represents the User information."""

    def __init__(self, username: str, grants: dict):
        self.__username = username
        self.__grants = grants

    def get_username(self):
        """This method returns the username."""
        return self.__username

    def is_grant(self, grant: bool):
        """This method returns if the user has a grant."""
        return self.__grants


class Authentication:
    """This class is used to validate users authentication."""

    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__grants = None

    def authenticate(self) -> bool:
        """This method validates the user credentials."""
        # Build the path to the users.json file dynamically, to be available anywhere.
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "users.json")
        
        
        with open(file_path, "r", encoding="UTF-8") as file:
            users = json.load(file)

        for user in users:
            if (
                user["username"] == self.__username
                and user["password"] == self.__password
            ):
                self.__grants = user["grants"]
                return True
          
        return False


        
    def userdata(self) -> User:
        """This method returns the user data."""
        return User(self.__username, self.__grants)

    def register(self, grants: dict):
        """This method registers a new user."""
        # Build the path to the users.json file dynamically, to be available anywhere.
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "users.json")

        new_user = {
            "username": self.__username,
            "password": self.__password,
            "grants": grants
        }

        with open(file_path, "r+", encoding="UTF-8") as file:
            users = json.load(file)
            users.append(new_user)
            file.seek(0)
            json.dump(users, file, indent=4)

        self.__grants = grants