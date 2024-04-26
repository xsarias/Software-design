"""
This file represents the log in system of the Vehicle Constructor application.

Author: Xiomara Arias - xsariasa@udistrital.edu.co
"""
from abc import ABC, abstractmethod
from datetime import datetime


# LogInSystem interface
class LoginSystem(ABC):
    '''This class represents a login system interface'''
    @abstractmethod
    def register(self):
        '''This method requests user data and saves information to create an account'''

# RealLogInSystem Class
class RealLogInSystem(LoginSystem):
    '''This class represents a real Log in'''
    def __init__(self, user_name:str, password:str, user_type:str):
       '''Constructor of RealLogInSystem Class'''
       self.user_name = user_name
       self.password = password
       self.user_type = user_type
    
    
    def register(self):
        '''This method requests user data and saves information to create an account'''
        print(f"--->WELCOME '{self.user_name}', now, you can enjoy the catalog.")
        return f"Name user:'{self.user_name}', Password:'{self.password}', Type:' {self.user_type}'\n"
   

# ProxyLogInSystem class
class ProxyLogInSystem(LoginSystem):
    '''This class represents a Proxy Log In System'''
    def __init__(self, user_name: str, password: str, user_type: str):
        '''Constructor of ProxyLogInSystem Class'''
        self.user_name = user_name
        self.password = password
        self.user_type = user_type
    
    def authentication(self):
        '''This method gets user data and verifies if the user trying to log in already exists.'''
        try:
            with open("logs.txt", "r") as file:
                for line in file:
                    # Check if the user line exists in the file
                    if f"Name user:'{self.user_name}', Password:'{self.password}', Type:'{self.user_type}'" in line:
                        # If the user exists, return True
                  
                        return True
        except FileNotFoundError:
            # in case the 
            print("The file logs.txt doesn't exist.")
        # If the user was not found in the file, return False
        return False
    

    def register(self):
        '''This method requests user data and saves information to create an account'''
        # First validate the data
        if self.authentication():
            print("User already exists. Registration aborted.")
            return 
        
        try:
            with open("logs.txt", "a") as file:
                file.write(
                    f"Name user:'{self.user_name}', Password:'{self.password}', Type:'{self.user_type}'\n"
                )
            print("User information successfully saved.")
        except (IOError, PermissionError) as e:
            print(f"Error writing to logs.txt: {e}")
    
        # Create instance for RealLogInSystem and register user.
        real_login_system = RealLogInSystem(self.user_name, self.password, self.user_type)
        real_login_system.register()

    def sig_In(self):
            '''This method requests user data and search on it, to sig in'''
            # First validate the data
            if self.authentication():
                print("-------------------***-------------------")
                print(f"--->WELCOME '{self.user_name}', now, you can enjoy the catalog.")
                return True
            
            try:
                with open("logs.txt", "a") as file:
                    file.write(
                        f"Name user:'{self.user_name}', Password:'{self.password}', Type:'{self.user_type}'\n"
                    )
                    real_login_system = RealLogInSystem(self.user_name, self.password, self.user_type)
                    real_login_system.register()
            except (IOError, PermissionError) as e:
                print(f"Error writing to logs.txt: {e}")
        
            # Create instance for RealLogInSystem and register user.
            

# Client Application
#log_in_system = ProxyLogInSystem("XOMssIddTAo", "43dd14", "adddmin")
#log_in_system.register()
