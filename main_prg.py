
class Garage_in():
    """Class and method to hold/give/recieve tickets & parking spaces"""
    def __init__(self):
        self.tickets = 10
        self.open_spaces = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
        self.closed_spaces = []
        self.currentTicket = {"Paid": False}
        self.car_info = []
        self.car_reciepts = []

#collecting driver information from Garage Class 
    def register(self):
        vehicle_type = input("Please enter vehicle type, ex. car, truck, suv etc.: ").lower()
        make = input("Please enter the make: ").lower()
        model = input("Please enter the model: ").lower()
        plate_ID = input("Please enter the plate_ID: ").lower()

        vec_reg = Garage(vehicle_type, make, model, plate_ID)
        self.car_info.append(vec_reg)
          
#Method to execute taking ticket and parking space. 
    def enter_garage(self):
        if self.tickets > 0:
            driver_response1 = input("Select lot you would like to reserve: [P1], [P2], [P3], [P4], [P5], [P6], [P7], [P8], [P9], [P10] ")
            if driver_response1.lower() == "p1" or "p2" or "p3" or "p4" or "p5" or "p6" or "p7" or "p8" or "p9" or "p10":
                self.open_spaces.remove(driver_response1.upper())
                self.closed_spaces.append(driver_response1.upper())
                print(f"\nYou have reserved {driver_response1}, Please take your ticket.")
                print("If you forgot to register your vechile we are not liable for any lost or damages.")
                self.tickets -= 1
        elif self.tickets <= 0:
                print(f"We have {self.tickets} available in our garage, please try again later")

#payment process options
    def pay_process(self):
        driver_response1 = input("\nWould you like to now or later? Type '1' for NOW or '2' for Later: ")
        if driver_response1.lower() == '1':
            self.exit_garage_now()
        elif driver_response1.lower() == '2':
            self.exit_garage_Later()
         
#When driver returns a ticket parking space and ticket count will increment by 1"""
#user will get a reciept after they finish.
#DID NOT ADD FAIL SAFES- IF user entered in incorrect parking lot id.
    def exit_garage_now(self):

        if self.currentTicket["Paid"] == False:
            driver_response3 = input("Select lot you are returning: [P1], [P2], [P3], [P4], [P5], [P6], [P7], [P8], [P9], [P10] ")
            if driver_response3.lower() == "p1" or "p2" or "p3" or "p4" or "p5" or "p6" or "p7" or "p8" or "p9" or "p10":
                print("\nYour ticket has been paid. You have 15 minutes to leave.")
                self.reciept()         
                self.closed_spaces.remove(driver_response3.upper())
                self.open_spaces.append(driver_response3.upper())
            self.tickets += 1

            return

    def exit_garage_Later(self):
#When driver returns a ticket parking space and ticket count will increment by 1"""
        if self.currentTicket["Paid"] == False:
            print("You have not paid your ticket, remember your parking spot ID. When you want to exit the parking garage")
            return

#Driver information given to them upon exit-garage-now.
    def reciept(self):

        for exit_ticket in self.car_info:
            print("---RECIEPT---")
            print(f"Vehicle Type: {exit_ticket.vehicle_type}")
            print(f"Make: {exit_ticket.make}")
            print(f"Model: {exit_ticket.model}")
            print(f"Plate_ID: {exit_ticket.plate_ID}")
            print(f"\nPAID $15.00")
            print("Thank you, have a nice day!")
            self.car_reciepts.append(exit_ticket)
    
#driver/user access point to parking lot. 
    def run(self):
        while True:
            driver_choice = input("\nParking today: '1' to register. '2' for ticket. '3' for pay. 'q' to quit:  ")

            if (driver_choice) == "1":
                self.register()
            elif (driver_choice) == "2":
                self.enter_garage()
            elif (driver_choice) == "3":
                self.pay_process()
            elif driver_choice.lower() == "q":
                return

#Class - attributes of  driver information
class Garage():
    def __init__(self,vehicle_type, make, model, plate_ID):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.plate_ID = plate_ID

spend = Garage_in()
spend.run()
