from Node import *


class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    
    def print_queue(self):

        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.length ==0 or self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -=1
        
        return temp
    

my_queue = Queue(1)
print('------queue at initalization-----')

my_queue.print_queue()
print('------enqueued 2-----')
my_queue.enqueue(2)

my_queue.print_queue()

print('------dequeued first object-----')
print(my_queue.dequeue())

print('------dequeued second object-----')
print(my_queue.dequeue())

my_queue.print_queue()