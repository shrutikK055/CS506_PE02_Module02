# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Dog class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Puppy class inherits from Dog
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Create an object of Puppy class
puppy = Puppy()

# Call methods from all levels of the class hierarchy
puppy.speak()
puppy.bark()
puppy.weep()
