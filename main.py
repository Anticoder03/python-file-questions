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
            print("✅ Correct guess! +20 points")
            score += 20
        else:
            print("❌ Wrong guess! -15 points")
            score -= 15

        current_card = next_card
        print(f"Current Score: {score}")
        print("--------------------------------------------------")

    print("\n🎮 Game Over!")
    print(f"Your Final Score: {score}")
    print("--------------------------------------------------")

# Run the game
if __name__ == "__main__":
    card_game()



