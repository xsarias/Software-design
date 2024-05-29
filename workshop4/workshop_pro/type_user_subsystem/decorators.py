from datetime import datetime
from .user_base import UserBase

class UserDecorator(UserBase):
    """This class represents a user type checking decorator for applications."""

    def __init__(self, user: UserBase, required_type: str):
        self.wrapped = user
        self.required_type = required_type

    def suscribe_to_newsletter(self, email):
        print(f"User: Subscribed {email} to newsletter")

    def check_user_type(self, request):
        if request.user_type != self.required_type:
            raise PermissionError(f"Access denied for users of type '{request.user_type}'. Required type: '{self.required_type}'")

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

class AdminDecorator(UserBase):
    """This class represents a monitoring decorator for admin applications."""

    def __init__(self, user: UserBase):
        self.wrapped = user

    def check_admin(self, request):
        if request.user_type != 'admin':
            raise PermissionError(f"Access denied for users of type '{request.user_type}'. Required type: 'admin'")
        self.__monitor_start()

    def __monitor_start(self):
        print(f"== Monitoring started at: {datetime.now()}")

    def __monitor_end(self):
        print(f"== Monitoring ended at: {datetime.now()}\n")

    def add_vehicle(self, attr_vehicles):
        print(f"Admin: Adding vehicle with attributes {attr_vehicles}")

    def delete_vehicle(self, model):
        print(f"Admin: Deleting vehicle model {model}")

    def send_news(self, list_subscribers):
        print(f"Admin: Sending news to subscribers: {list_subscribers}")

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)
