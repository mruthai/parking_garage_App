
currentTicket = {
    i:True for i in range(1,11)
}
def assign_ticket():
    for ticket,paid in currentTicket.items():

        if not paid:
            #current ticket
            print(ticket," is available")
            currentTicket[ticket] = False
        
            break  
    return ticket                     

# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()
# assign_ticket()

# print(assign_ticket)

print(currentTicket)


# print(examplegenerator)

# # park = recieving_ticket
#         for t in recieving_ticket
#         remove_tickets = Product(park)
#         self.ticket.append(remove_tickets)
#         for i in range(self.ticket):
#             if self.ticket[i].ticket == :

