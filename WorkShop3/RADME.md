# Workshop 3 - Solution

This is a workshop related with a backend system to provide a vehicles catalog using python and patterns design lie structural patterns.

## Requirements

The requirements for this workshop are presented as follows:
- Application is still consuming a lot of memory, so you must reduce it as much as possible.
- An authentication system is needed, so you must create a simple login system where you could register users and authenticate them.
- You should differentiate two types of users: Admin and User. Admins could create, update, and delete vehicles, while Users could only see and search the vehicles.
- You should log all the actions made by the users, so you could track both the changes made in the vehicles and searches performed.
- Separate your project in different subsystems, and a made a simple interface to interact with them.

## Business Rules

- Admin can create, delete, and update vehicles.
- A user can only view and search vehicles.
- A client can interact with two different facades, according to their type.
- The client must log in before starting to interact with the application."
