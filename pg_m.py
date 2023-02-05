# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking

# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary



class Garage_in():
    """Class and method to hold/give/recieve tickets & parking spaces"""
    def __init__(self):
        self.tickets = 10
        self.open_spaces = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
        self.closed_spaces = []
        self.currentTicket = {"Paid": False}
          

#Method to execute taking ticket and parking space. 
    def enter_garage(self):
        if self.tickets > 0:
            driver_response1 = input("Select lot you would like to reserve: [P1], [P2], [P3], [P4], [P5], [P6], [P7], [P8], [P9], [P10] ")
            if driver_response1.lower() == "p1" or "p2" or "p3" or "p4" or "p5" or "p6" or "p7" or "p8" or "p9" or "p10":
                self.open_spaces.remove(driver_response1.upper())
                self.closed_spaces.append(driver_response1.upper())
                print(f"You have reserved {driver_response1}, Please take your ticket.")
                self.tickets -= 1
        elif self.tickets <= 0:
                print(f"We have {self.tickets} available in our garage, please try again later")

        driver_response1 = input("Would you like to now or later? Type '1' for NOW or '2' for Later: ")
        if driver_response1.lower() == '1':
            self.exit_garage1()
        elif driver_response1.lower() == '2':
            self.exit_garage2()
         

    def exit_garage1(self):
#When driver returns a ticket parking space and ticket count will increment by 1"""

        # if self.currentTicket["Paid"] == False:
            
            # driver_response3 = input(f"Please enter your ticket number: ")

        if self.currentTicket["Paid"] == True:
            driver_response3 = input("Select lot you are returning: [P1], [P2], [P3], [P4], [P5], [P6], [P7], [P8], [P9], [P10] ")
            if driver_response3.lower() == "p1" or "p2" or "p3" or "p4" or "p5" or "p6" or "p7" or "p8" or "p9" or "p10":
                self.closed_spaces.remove.remove(driver_response3.upper())
                self.open_spaces.append(driver_response3.upper())
            print("Your ticket has been paid $15 dollars, you have 15 minutes to leave.")
            print("Thank you, have a nice day!")
            self.tickets += 1
            return

    def exit_garage2(self):
#When driver returns a ticket parking space and ticket count will increment by 1"""
        print("You have not paid your ticket")
        if self.currentTicket["Paid"] == False:
            print("Your ticket has been paid $15 dollars, you have 15 minutes to leave.")
            print("Thank you, have a nice day!")
            return

    def run(self):
        while True:
            driver_choice = input("Parking today? (y/n) or quit: ")

            if driver_choice.lower() == "y":
                self.enter_garage()
            elif driver_choice.lower() == "n":
                
                return

class Garage():
    def __init__(self,tickets,park_space,payment):
        self.tickets = tickets
        self.park_space = park_space
        self.payment = payment
        

spend = Garage_in()
spend.run()


#    def pay_now(self):
#         self.payment

#         place_payment = int(input("Parking = $12.00 Please type '12': "))
#         if place_payment == True:
#             print("Thanks for your business you have 15 minutes to leave")
#         else:
#             self.enter_garage()

# # car_driver_pay_later = 
#     def pay_later(self):
#         later_payment = int(input("Parking = $12.00 Please type '12': "))
#         if later_payment == True:
#             self.enter_garage()
    
                
#     def tickets_in_out(self):
#         pass