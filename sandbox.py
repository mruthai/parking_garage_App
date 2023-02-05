
examplegenerator = {
    i:False for i in range(1,4)
}
def assign_ticket():
    for ticket,paid in examplegenerator.items():
        if not paid:
            print(ticket," is available")
            examplegenerator[ticket] = True
        
            break  
    return ticket                     



print(examplegenerator)


# print(examplegenerator)

#

