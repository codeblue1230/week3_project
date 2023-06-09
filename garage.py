"""
-Take ticket method
-Parking spaces available method
-Tracking ticket (paid/not paid)
-Random Parking garage number

"""

class Garage():
    def __init__(self):
        self.ticket = None
        self.parking_spaces = None
        self.tracking = None
        self.parked_car = {}

    def take_ticket(self):
        
        print("Welcome to the Maryan Garage! The prices are as listed: ")
        response = input("Level 1 - $10, Level 2 - $8, Level 3 through 7 - $5 \n Which level would you like to park at?")
        if response.lower() == "level 1":
            
            self.parked_car['level'] = response
            self.parked_car['price'] = 10
        
            print(f"You parked on {self.parked_car['level'].title()}! When you leave you owe {self.parked_car['price']} dollars!")

        elif response.lower() == "level 2":

            self.parked_car['level'] = response
            self.parked_car['price'] = 8
            print(f"You parked on {self.parked_car['level'].title()}! When you leave you owe {self.parked_car['price']} dollars!")

        elif response.lower() == "level 3" or "level 4" or "level 5" or "level 6" or "level 7":
            
            self.parked_car['level'] = response
            self.parked_car['price'] = 5
            print(f"You parked on {self.parked_car['level'].title()}! When you leave you owe {self.parked_car['price']} dollars!")

        else:
            print("Please input a valid response!")
            



    def run(self):

        while True:
            response = input(f"Hi there! There are {self.parking_spaces} parking spaces available! Do you want to take a ticket? y/n ")
            if response.lower() in ('y', 'yes'):
                self.take_ticket()
                break
            #elif:  
            #    print()

maryan = Garage()

maryan.run()


