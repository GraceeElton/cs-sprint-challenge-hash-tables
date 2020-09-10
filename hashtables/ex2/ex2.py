#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        # they said to link so we need to use a linkedlist within a hashmap
        # We can hash each ticket such that the starting location is the key and
        # the destination is the value.


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE

    """
    d = {}
    route = []

    # Your code here
    # okay so need to go through each item and make it a key
    # then we need to find the which item is matches the next value
    # and go in order until we reach our stop word which is NONE w

    # okay so need to go through each item and make it a key
    for i in tickets:
        d[i.source] = i.destination
    # find the start ticket wich is equal to NONE
    route.append(d['NONE'])

    for i in range(1, length):
        # route, the `i`th location in the route can be found by checking the
        # hash table for the `i-1`th location.
        next_source = route[i-1]
        if next_source in d:
            route.append(d[next_source])
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)
