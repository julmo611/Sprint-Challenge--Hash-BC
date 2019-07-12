#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    index = 0
    search_index = 0
    search_parameter = "NONE"
    while None in route:
        if index == length:
            index = 0
        if tickets[index].source == search_parameter:
            route[search_index] = tickets[index].destination
            search_parameter = tickets[index].destination
            search_index += 1
            index = 0
        elif tickets[index].source != search_parameter:
            index += 1
    return route


def tickets():
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
               ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    result = reconstruct_trip(tickets, 10)

    print(result)


tickets()
