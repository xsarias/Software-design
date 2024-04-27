"""
This file represents a interface login application of the Catalog from Vehicle Constructor Company.

Author: Xiomara Arias - xsariasa@udistrital.edu.co
"""
from LogInSystem import *
from CatalogFacade import *

#Facade Class
class LogInFacade:
    '''this class represent a Log In facade of Vehicle Constructor Application'''
    def __init__(self, user_name, password, type, action):
        #self.clientRequest=ClientRequest()
        self.user_name=user_name
        self.password=password
        self.type=type
        self.action=action
        self.login_system=ProxyLogInSystem(self.user_name, self.password, self.type)
        if self.action=="LogIn":
            self.login_system.sig_In()
        elif self.action=="SignUp":
            self.login_system.register()

        if self.type=="user":
            userFacade=User(self.user_name)
            userFacade.run()
        elif self.type=="admin":
            adminFacade=Admin(self.user_name)
            adminFacade.run()
        
        
def logInMenu():
        '''this method shows the Login Menu'''
        # ==================================== MENU
        MESSAGE = """
        >>> WELCOME TO VEHICLE CONSTRUCTOR APP<<
        1). Log in.
        2). Sign up.
        3). Exit.
        """
        print(MESSAGE)
        option = int(input("->Please, choise an option: "))
        while option != 3:
            if option == 1:
                print(">>>>>>--- LOG IN ---<<<<<<")
                action="LogIn"
                user_name = input("User Name -->")
                password=input("Password -->")
                print("Type of user: user(1) or admin(2)")
                option = int(input("->Please, choise an option:"))
                if option==1:
                    type="user"
                elif option==2:
                    type="admin"
                catalog=LogInFacade(user_name, password, type, action)
                break
            elif option == 2:
                print(">>>>>>--- SIGN UP ---<<<<<<")
                action="SignUp"
                print("welcome to Vehicle constructor, please provide the following information to register you")
                user_name = input("User Name -->")
                password = input("Password -->")
                print("Type of user: user(1) or admin(2)")
                option = int(input("->Please, choise an option:"))
                if option==1:
                    type="user"
                elif option==2:
                    type="admin"
                catalog=LogInFacade(user_name, password, type, action)
                break
                
#-----------------cliente             
logInMenu()