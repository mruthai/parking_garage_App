
currentTicket = {
    i:False for i in range(1,201)
}
def assign_ticket():
    for ticket,paid in currentTicket.items():
        if not paid:
            print(ticket," is available")
            currentTicket[ticket] = True
        
            break  
    return ticket                     

assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()
assign_ticket()

print(currentTicket)


# print(examplegenerator)

#

