# Quiz1

#Question1
def recursive_multiply(x, y):
   if x == 0:
      return 0
   elif x == 1:
      return y
   else:
      return y + recursive_multiply(x-1, y)

# Question2
class Ticket:
    counter = 0
    def __init__(self):
        self.ticket_number = Ticket.counter
        if Ticket.counter == 99:
            Ticket.counter = 0
        else:
            Ticket.counter += 1
for ticket in range(0, 100):
    my_ticket = Ticket()
    print(my_ticket.ticket_number)