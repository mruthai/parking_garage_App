

class Garage_in():
    """Class and method to hold/give/recieve tickets & parking spaces"""
    def __init__(self):
        self.ticket = []
        self.park_space = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
                    #ticket id 
        self.ticket_num = { i:True for i in range(1,11) 
        }

# Method to enter garage for accessing 2 payment types
    def enter_garage(self):
        self.tic_taken = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','t10']

        ticket_choice = input(" Type '1' for ticket or '2' to exit: ")
    
        ticket_choice == "1":
    

        # i in range(len(self.ticket))
        #     if self.ticket[i] == ticket_choice:
        #         self.ticket
        # else:
        #     ticket_choice == "2"
        #     print("Reminder to pay later")
        #     self.pay_later()

    def tickets(self):
        return self.ticket
        

    def pay_now(self):
        place_payment = int(input("Parking = $12.00 Please type '12': "))
        if place_payment == True:
            print("Thanks for your business you have 15 minutes to leave")
        else:
            self.enter_garage()

# car_driver_pay_later = 
    def pay_later(self):
        later_payment = int(input("Parking = $12.00 Please type '12': "))
        if later_payment == True:
            self.enter_garage()
    
                
    def tickets_in_out(self):
        pass
    
    def exit_garage(self):
        return

    def run(self):
            driver_choice = input("Parking today? (y/n): ")

            if driver_choice == "y":
                self.enter_garage()
            elif driver_choice == "n":
                self.exit_garage()
                return
            
                
                


class Garage():
    def __init__(self,ticket,park_space,ticket_num):
        self.ticket = ticket
        self.park_space = park_space
        self.ticket_num = ticket_num

    


        

spend = Garage_in()
spend.run()