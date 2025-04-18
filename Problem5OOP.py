# Define a User class
class User:
    def __init__(self, first_name, last_name, age, email):
        # Store the user's information
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    # Method to print user details
    def describe(self):
        print("Name:", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)

    # Method to greet the user
    def greet(self):
        print("Hello,", self.first_name)
        print()  # Print a blank line

# Create two users with their info
user1 = User("Alice", "Smith", 30, "alice@example.com")
user2 = User("Bob", "Jones", 25, "bob@example.com")

# Show info and greeting for user1
user1.describe()
user1.greet()

# Show info and greeting for user2
user2.describe()
user2.greet()
