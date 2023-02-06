# parking_garage_W2

There are 2 class that run the parking garage- opp
1. The garage class that contains all the information that the user will provide the parking lot.
2. The garage_in class that houses the method and attributes that will remain constant for the park garage to operatate but also keep the information the user provides. 

The user has 3 options when they enter the garage. 1. register their vehicle. 2. get a ticket. 3. pay for their parking space.

The program was designed with the assumption that the user would follow the order of the inputs above. 

BUGS:
1. There is not a fail safe if the user inputs the wrong ticket information.
2. If a user exits the parking lot after they paid and another user take's their parking spot. 
  After the second or more users takes and pays through the same parking spot. The printed reciept will print- previous users information.
3. There isn't a fail safe for incorrect information. 
