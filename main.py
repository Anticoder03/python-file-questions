# Q1. . Write a Python program to demonstrate multiple inheritance.
# 1. Employee class has 3 data members EmployeeID, Gender (String), Salary and
# PerformanceRating(Out of 5) of type int. It has a get() function to get these details from
# the user.
# 2. JoiningDetail class has a data member DateOfJoining of type Date and a function
# getDoJ to get the Date of joining of employees.
# 3. Information Class uses the marks from Employee class and the DateOfJoining date
# from the JoiningDetail class to calculate the top 3 Employees based on their Ratings
# and then Display, using readData, all the details on these employees in Ascending
# order of their Date Of Joining.


from datetime import datetime

# Base Class 1
class Employee:
    def __init__(self):
        self.EmployeeID = None
        self.Gender = None
        self.Salary = 0
        self.PerformanceRating = 0

    def get(self):
        self.EmployeeID = input("Enter Employee ID: ")
        self.Gender = input("Enter Gender (M/F): ")
        self.Salary = float(input("Enter Salary: "))
        self.PerformanceRating = int(input("Enter Performance Rating (out of 5): "))

# Base Class 2
class JoiningDetail:
    def __init__(self):
        self.DateOfJoining = None

    def getDoJ(self):
        doj_str = input("Enter Date of Joining (YYYY-MM-DD): ")
        self.DateOfJoining = datetime.strptime(doj_str, "%Y-%m-%d")

# Derived Class using Multiple Inheritance
class Information(Employee, JoiningDetail):
    def __init__(self):
        Employee.__init__(self)
        JoiningDetail.__init__(self)

    def readData(self):
        print(f"Employee ID: {self.EmployeeID}")
        print(f"Gender: {self.Gender}")
        print(f"Salary: {self.Salary}")
        print(f"Rating: {self.PerformanceRating}")
        print(f"Date of Joining: {self.DateOfJoining.strftime('%Y-%m-%d')}")
        print("-" * 40)

# Main Program
def main():
    n = int(input("Enter number of employees: "))
    employees = []

    # Get details for each employee
    for i in range(n):
        print(f"\nEnter details for Employee {i + 1}")
        emp = Information()
        emp.get()
        emp.getDoJ()
        employees.append(emp)

    # Sort by PerformanceRating descending (top 3)
    top3 = sorted(employees, key=lambda e: e.PerformanceRating, reverse=True)[:3]

    # Sort top3 by DateOfJoining ascending
    top3_sorted = sorted(top3, key=lambda e: e.DateOfJoining)

    print("\nTop 3 Employees (by rating) in ascending order of Date of Joining:\n")
    for emp in top3_sorted:
        emp.readData()

# Run Program
if __name__ == "__main__":
    main()



# Q.2 Write a Python program to demonstrate Polymorphism.
# 1. Class Vehicle with a parameterized function Fare, that takes input value as fare and
# returns it to calling Objects.
# 2. Create five separate variables Bus, Car, Train, Truck and Ship that call the Fare
# function.
# 3. Use a third variable TotalFare to store the sum of fare for each Vehicle Type.
# 4. Print the TotalFare.


# Base Class
class Vehicle:
    def Fare(self, fare):
        return fare

# Derived Classes demonstrating Polymorphism
class Bus(Vehicle):
    def Fare(self, fare):
        print("Bus Fare:", fare)
        return fare

class Car(Vehicle):
    def Fare(self, fare):
        print("Car Fare:", fare)
        return fare

class Train(Vehicle):
    def Fare(self, fare):
        print("Train Fare:", fare)
        return fare

class Truck(Vehicle):
    def Fare(self, fare):
        print("Truck Fare:", fare)
        return fare

class Ship(Vehicle):
    def Fare(self, fare):
        print("Ship Fare:", fare)
        return fare

# Create objects
bus = Bus()
car = Car()
train = Train()
truck = Truck()
ship = Ship()

# Call Fare() polymorphically
TotalFare = (
    bus.Fare(200) +
    car.Fare(150) +
    train.Fare(300) +
    truck.Fare(400) +
    ship.Fare(1000)
)

print("\nTotal Fare for all Vehicles:", TotalFare)




# Q3.  Consider an ongoing test cricket series. Following are the names of the players and their
# scores in the test1 and 2.
# Test Match 1 :
# Dhoni : 56 , Balaji : 94
# Test Match 2 :
# Balaji : 80 , Dravid : 105
# Calculate the highest number of runs scored by an individual cricketer in both of the matches.
# Create a python function Max_Score (M) that reads a dictionary M that recognizes the player
# with the highest total score. This function will return ( Top player , Total Score ) . You can
# consider the Top player as String who is the highest scorer and Top score as Integer .
# Input : Max_Score({‘test1’:{‘Dhoni’:56, ‘Balaji : 85}, ‘test2’:{‘Dhoni’ 87, ‘Balaji’’:200}})
# Output : (‘Balaji ‘ , 200)

def Max_Score(M):
    total_scores = {}

    # Loop through each test match
    for match, players in M.items():
        for player, score in players.items():
            # Add scores cumulatively
            if player in total_scores:
                total_scores[player] += score
            else:
                total_scores[player] = score

    # Find the player with the highest total
    top_player = max(total_scores, key=total_scores.get)
    top_score = total_scores[top_player]

    return (top_player, top_score)


# Example Input
M = {
    'test1': {'Dhoni': 56, 'Balaji': 94},
    'test2': {'Balaji': 80, 'Dravid': 105}
}

# Call the function
result = Max_Score(M)

# Display Output
print("Top Scorer:", result)


# Q4. Create a simple Card game in which there are 8 cards which are randomly chosen from a
# deck. The first card is shown face up. The game asks the player to predict whether the next card
# in the selection will have a higher or lower value than the currently showing card.
# For example, say the card that’s shown is a 3. The player chooses “higher,” and the next card is
# shown. If that card has a higher value, the player is correct. In this example, if the player had
# chosen “lower,” they would have been incorrect. If the player guesses correctly, they get 20
# points. If they choose incorrectly, they lose 15 points. If the next card to be turned over has the
# same value as the previous card, the player is incorrect.



import random

def card_game():
    # Generate 8 random cards (values between 1 and 13)
    cards = random.sample(range(1, 14), 8)
    score = 0

    print("🃏 Welcome to the Higher or Lower Card Game!")
    print("--------------------------------------------------")
    print("Cards have values from 1 (Ace) to 13 (King).")
    print("You get +20 for correct guess, -15 for wrong guess.")
    print("--------------------------------------------------")

    current_card = cards[0]
    print(f"\nStarting card: {current_card}")

    # Loop through remaining cards
    for i in range(1, len(cards)):
        guess = input("Will the next card be Higher (H) or Lower (L)? ").strip().upper()
        next_card = cards[i]

        print(f"Next card: {next_card}")

        # Determine result
        if (guess == 'H' and next_card > current_card) or (guess == 'L' and next_card < current_card):
            print(" Correct guess! +20 points")
            score += 20
        else:
            print(" Wrong guess! -15 points")
            score -= 15

        current_card = next_card
        print(f"Current Score: {score}")
        print("--------------------------------------------------")

    print("\n Game Over!")
    print(f"Your Final Score: {score}")
    print("--------------------------------------------------")

# Run the game
if __name__ == "__main__":
    card_game()



# Q5. Create an empty dictionary called Car_0 . Then fill the dictionary with Keys : color , speed
# , X_position and Y_position.
# car_0 = {'x_position': 10, 'y_position': 72, 'speed': 'medium'} .
# a) If the speed is slow the coordinates of the X_pos get incremented by 2.
# b) If the speed is Medium the coordinates of the X_pos gets incremented by 9
# c) Now if the speed is Fast the coordinates of the X_pos gets incremented by 22.
# Print the modified dictionary.
# creating empty dictionary
car_0 = {}

# filling the dictionary
car_0['color'] = 'red'
car_0['speed'] = 'medium'
car_0['x_position'] = 10
car_0['y_position'] = 72

print("Before update:", car_0)

# update x_position based on speed
if car_0['speed'] == 'slow':
    car_0['x_position'] += 2
elif car_0['speed'] == 'medium':
    car_0['x_position'] += 9
elif car_0['speed'] == 'fast':
    car_0['x_position'] += 22

print("After update:", car_0)



# Q6. Show a basic implementation of abstraction in python using the abstract classes.
# 1. Create an abstract class in python.
# 2. Implement abstraction with the other classes and base class as abstract class.

from abc import ABC, abstractmethod

# abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# implementing abstraction
class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

    def stop(self):
        print("Car stops when brakes are applied.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start.")

    def stop(self):
        print("Bike stops using hand brakes.")

# using the classes
c = Car()
b = Bike()

c.start()
c.stop()

b.start()
b.stop()


# Q7. Create a program in python to demonstrate Polymorphism.
# 1. Make use of private and protected members using python name mangling techniques.
class Animal:
    def __init__(self, name):
        self._type = "Animal"       # protected
        self.__name = name          # private

    def speak(self):
        return "Some sound"

    def get_name(self):
        return self.__name  # accessing private member

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# polymorphism demo
animals = [Dog("Tommy"), Cat("Kitty")]

for a in animals:
    print(a.get_name(), "says", a.speak())

# accessing private using name mangling
dog = Dog("Sheru")
print("Private name using mangling:", dog._Animal__name)



# Q8. Given a list of 50 natural numbers from 1-50. Create a function that will take every element
# from the list and return the square of each element. Use the python map and filter methods to
# implement the function on the given list.
numbers = list(range(1, 51))

# function to square a number
def square(n):
    return n * n

# map for squares
squared = list(map(square, numbers))

# filter example: keep only even squares
even_squares = list(filter(lambda x: x % 2 == 0, squared))

print("Squares:", squared)
print("Even Squares:", even_squares)


# Q9. Create a class, Triangle. Its init() method should take self, angle1, angle2, and angle3 as
# arguments.
class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

t = Triangle(60, 60, 60)
print(t.angle1, t.angle2, t.angle3)


# Q10. Create a class variable named number_of_sides and set it equal to 3.

class Triangle:
    number_of_sides = 3   

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

t = Triangle(60, 60, 60)
print("Number of sides:", Triangle.number_of_sides)
print("Angles:", t.angle1, t.angle2, t.angle3)

# Q11. Create a method named check_angles. The sum of a triangle's three angles should return
# True if the sum is equal to 180, and False otherwise. The method should print whether the
# angles belong to a triangle or not.
# 11.1 Write methods to verify if the triangle is an acute triangle or obtuse triangle.
# 11.2 Create an instance of the triangle class and call all the defined methods.
# 11.3 Create three child classes of triangle class - isosceles_triangle, right_triangle and
# equilateral_triangle.
# 11.4 Define methods which check for their properties.
class Triangle:
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    # 11. Check if angles form a valid triangle
    def check_angles(self):
        total = self.angle1 + self.angle2 + self.angle3
        if total == 180:
            print(" These angles form a valid triangle.")
            return True
        else:
            print(" These angles do NOT form a triangle.")
            return False

    # 11.1 Check acute triangle (all angles < 90)
    def is_acute(self):
        if (self.angle1 < 90 and self.angle2 < 90 and self.angle3 < 90):
            print(" This is an Acute Triangle.")
            return True
        print(" Not an Acute Triangle.")
        return False

    # 11.1 Check obtuse triangle (one angle > 90)
    def is_obtuse(self):
        if (self.angle1 > 90 or self.angle2 > 90 or self.angle3 > 90):
            print(" This is an Obtuse Triangle.")
            return True
        print(" Not an Obtuse Triangle.")
        return False


#  11.3 — Child Classes
class IsoscelesTriangle(Triangle):
    def is_isosceles(self):
        if (self.angle1 == self.angle2 or 
            self.angle2 == self.angle3 or 
            self.angle1 == self.angle3):
            print(" This is an Isosceles Triangle.")
            return True
        print(" Not an Isosceles Triangle.")
        return False


class RightTriangle(Triangle):
    def is_right(self):
        if (self.angle1 == 90 or self.angle2 == 90 or self.angle3 == 90):
            print(" This is a Right Triangle.")
            return True
        print(" Not a Right Triangle.")
        return False


class EquilateralTriangle(Triangle):
    def is_equilateral(self):
        if (self.angle1 == self.angle2 == self.angle3 == 60):
            print(" This is an Equilateral Triangle.")
            return True
        print(" Not an Equilateral Triangle.")
        return False


#  11.2 — Create instance & call methods
print("===== TRIANGLE INSTANCE CHECK =====")
t = Triangle(60, 60, 60)

t.check_angles()
t.is_acute()
t.is_obtuse()




# Q12. Create a class isosceles_right_triangle which inherits from isosceles_triangle and
# right_triangle.
# 12.1 Define methods which check for their properties.
class IsoscelesRightTriangle(IsoscelesTriangle, RightTriangle):
    def check_isosceles_right(self):
        iso = self.is_isosceles()
        right = self.is_right()

        if iso and right:
            print(" This is an Isosceles Right Triangle.")
            return True

        print(" Not an Isosceles Right Triangle.")
        return False


#  Testing Q12 class
print("\n===== ISOSCELES RIGHT TRIANGLE CHECK =====")
irt = IsoscelesRightTriangle(45, 45, 90)

irt.check_angles()
irt.is_isosceles()
irt.is_right()
irt.check_isosceles_right()
