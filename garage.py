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
        self.parking_spaces = {}
        self.payment = None
        self.parked_car = {}
        self.managers = None
        self.parking = None

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
        print(f"Thanks for parking at the Maryan Garage. You owe {self.parked_car['price']} dollars.")

        while True:
            response = int(input("Please input how much money you want to give: "))

            self.payment = response

            if self.payment == self.parked_car['price']:
                print("You gave us exact change. Have a nice day!")
                break
            
            elif self.payment < self.parked_car['price']:
                print(f"You gave us {self.payment}. You still owe us {self.parked_car['price'] - self.payment}.")
                owed_amount = self.parked_car['price'] - self.payment
                response = int(input("Please enter how much you owe us: "))
                if response == owed_amount:
                    print("Thank you for paying, have a nice day.")
                    break
                elif response < owed_amount:
                    print(f"You can leave, but you still owe us {owed_amount-response}. Please come back and pay us ASAP or face the consequences.")
                    break
                elif response > owed_amount:
                    print(f"Here's your change. We owe you {response - owed_amount} dollars. Thank you!")
                    break

            elif self.payment > self.parked_car['price']:
                print(f"Here's your change. We owe you {self.payment - self.parked_car['price']}")
                break

            elif self.payment < 0:
                print("Please enter a positive number. We need our money. Times are tough.")
            else:
                print("That's not a valid response! Please try again.")

    def manager(self):
        
        response = input("What would you like to do: track spaces, remove car, change managers")
        if response.lower() == "track spaces":
            
            for i in range(1, 8):

                park_space = list(range(1,100,1))
                space_filled = random.choice(park_space)

                self.parking_spaces['level'] = self.parked_car['level']

                if self.parking_spaces['level'] == f'level {i}':
                    self.parking_spaces[f"level {i}"] = space_filled - 1
                else:
                    self.parking_spaces[f"level {i}"] = space_filled

            

            for j in range(1, 8):
                if f'level {j}' == self.parking_spaces['level']:
                    print(f'Level {j}: {self.parking_spaces[f"level {j}"]} - User is on this level.')
                else:
                    print(f'Level {j}: {self.parking_spaces[f"level {j}"]}')
            
            
            
                

                
                # space_filled = random.choice(park_space)
                # self.parked_car["level 2"] = space_filled
                # if self.parked_car['level'] == 'level 2':
                #     self.parked_car["level 2"] = space_filled - 1

                
                # space_filled = random.choice(park_space)
                # self.parked_car["level 3"] = space_filled
                # if self.parked_car['level'] == 'level 3':
                #     self.parked_car["level 3"] = space_filled - 1

                
                # space_filled = random.choice(park_space)
                # self.parked_car["level 4"] = space_filled
                # if self.parked_car['level'] == 'level 4':
                #     self.parked_car["level 4"] = space_filled - 1

                
                # space_filled = random.choice(park_space)
                # self.parked_car["level 5"] = space_filled
                # if self.parked_car['level'] == 'level 5':
                #     self.parked_car["level 5"] = space_filled - 1

                
                # space_filled = random.choice(park_space)
                # self.parked_car["level 6"] = space_filled
                # if self.parked_car['level'] == 'level 6':
                #     self.parked_car["level 6"] = space_filled - 1

                
                # space_filled = random.choice(park_space)
                # self.parked_car["level 7"] = space_filled
                # if self.parked_car['level'] == 'level 7':
                #     self.parked_car["level 7"] = space_filled - 1

            
            

            


        # response = int(input(f"Thanks for parking at the Maryan Garage. You owe {self.parked_car['price']} dollars. Please choose the amount you are going to input: "))
        # self.payment = response

        
        # if self.payment == self.parked_car['price']:
        #     print("You gave us exact change. Have a nice day!")
            
        # elif self.payment < self.parked_car['price']:
        #     print(f"You gave us {self.payment}. You still owe us {self.parked_car['price'] - self.payment}.")

        # elif self.payment > self.parked_car['price']:
        #     print(f"Here's your change. We owe you {self.payment - self.parked_car['price']}")

        # elif self.payment < 0:
        #     print("Please enter a positive number.We need are money. Tmes are tough.")

        

    def run(self):

        while True:
            response = input(f"Hi there! There are {self.parking} parking spaces available! Do you want to take a ticket? y/n ")
            if response.lower() in ('y', 'yes'):
                self.take_ticket()
            
            response_2 = input(f"What do you want to do? leave garage, manager mode")
            if response_2.lower() == "leave garage":
                self.leave_garage()
            elif response_2.lower() == "manager mode":
                self.manager()
                
            #elif:  
            #    print()


maryan = Garage()

maryan.run()


