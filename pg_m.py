# Testing 

# Your parking *gargage class* should have the following methods:

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parking Spaces available by 1

# - pay For Parking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) 
#           -> display a message to the user that their ticket has been paid and they have 15mins to leave
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

class Ticket_container():
    def __init__(self):
        self.ticket = 200
        self.pk_space = 200
        self.currentTicket = {}

    
    def take_ticket(self):
        # ticket = input("")
        remove_tickets = Product(ticket)
        self.ticket.append(remove_tickets)
        for i in range(self.ticket):
            if self.ticket[i].ticket == 200:
                 -=
        

    def p_space(self):
        slot = 200
        for i in range(self.pk_space):
            if self.pk_space[i].ticket == slot:

    # def print_tk_reciept(self):
    #     for ticket_sales in self.tickts:
    #         print(f"Thank You, have a nice day{")

    def run(self):
        while True:
            car_driver = input("Garage Options (ticket/pay/leave)")

            if car_driver == "ticket":
                self.take_ticket()
            elif car_driver == "pay":
                self.
            elif car_driver == "leave":
                self.
            


class Product():
    def __init__(self, ticket, parkingSpaces, currentTicket):
        self.ticket = ticket
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

ticket_exchange = Ticket_container()
ticket_exchange.run()