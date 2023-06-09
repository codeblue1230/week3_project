"""
-Take ticket method
-Parking spaces available method
-Tracking ticket (paid/not paid)
-Random Parking garage number

"""
import random 

class Garage():
    def __init__(self):
        self.ticket = None
        self.parking_spaces = None
        self.payment = None
        self.parked_car = {}

    def take_ticket(self):
        parking_space_list = list(range(1,100,1))
        random_space = random.choice(parking_space_list)

        print("Welcome to the Maryan Garage! The prices are as listed: ")
        response = input("Level 1 - $10, Level 2 - $8, Level 3 through 7 - $5 \n Which level would you like to park at?")
        if response.lower() == "level 1":
            
            self.parked_car['level'] = response
            self.parked_car['price'] = 10
            self.parked_car['parking spot'] = random_space
        
            print(f"You parked on {self.parked_car['level'].title()}! Park in spot number {random_space}. When you leave you owe {self.parked_car['price']} dollars!")

        elif response.lower() == "level 2":

            self.parked_car['level'] = response
            self.parked_car['price'] = 8
            self.parked_car['parking spot'] = random_space

            print(f"You parked on {self.parked_car['level'].title()}! Park in spot number {random_space}. When you leave you owe {self.parked_car['price']} dollars!")

        elif response.lower() == "level 3" or "level 4" or "level 5" or "level 6" or "level 7":
            
            self.parked_car['level'] = response
            self.parked_car['price'] = 5
            self.parked_car['parking spot'] = random_space

            print(f"You parked on {self.parked_car['level'].title()}! Park in spot number {random_space}. When you leave you owe {self.parked_car['price']} dollars!")

        else:
            print("Please input a valid response!")

    def leave_garage(self):
        response = int(input(f"Thanks for parking at the Maryan Garage. You owe {self.parked_car['price']} dollars. Please choose the amount you are going to input: "))
        self.payment = response

        if self.payment == self.parked_car['price']:
            print("You gave us exact change. Have a nice day!")

        elif self.payment < self.parked_car['price']:
            print(f"You gave us {self.payment}. You still owe us {self.parked_car['price'] - self.payment}.")

        elif self.payment > self.parked_car['price']:
            print(f"Here's your change. We owe you {self.payment - self.parked_car['price']}")

        elif self.payment < 0:
            print("Please enter a positive number.We need are money. Tmes are tough.")

        

    def run(self):

        while True:
            response = input(f"Hi there! There are {self.parking_spaces} parking spaces available! Do you want to take a ticket? y/n ")
            if response.lower() in ('y', 'yes'):
                self.take_ticket()
            
            response_2 = input(f"Insert text here")
            if response_2.lower() == "leave garage":
                self.leave_garage()
                
            #elif:  
            #    print()

maryan = Garage()

maryan.run()


