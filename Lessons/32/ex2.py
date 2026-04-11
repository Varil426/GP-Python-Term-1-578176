"""
Utwórz symulator kolejki do kina, gdzie elementami kolejki są klienci razem z ich zamówieniem.
Do utworzenia symulatora kolejki użyj naszej struktury `Queue`, którą stworzyliśmy wcześniej.
"""

from Queue import Queue

class Customer:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def info(self):
        return f"Name: {self.name}, Order: {self.order}"

class CinemaQueue:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, name, order):
        self.queue.enqueue(Customer(name, order))
    
    def remove_customer(self):
        return self.queue.dequeue()
    
    def next_customer_order(self):
        return self.queue.peek()

queue = CinemaQueue()

queue.add_customer("Bartek", "Minecraft Movie")
queue.add_customer("Michał", "Kung Fu Panda 4")
queue.add_customer("Kacper", "Project Hail Mary")
queue.add_customer("Sebastian", "Deadpool & Wolverine")

print(queue.next_customer_order().info())
queue.remove_customer()

print(queue.next_customer_order().info())