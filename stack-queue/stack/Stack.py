from Node import *

class Stack:

    def __init__(self,value):

        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top 
        self.top = self.top.next 
        temp.next = None
        self.height -=1
        if self.height == 0:
            self.top = None
        return temp.value

my_stack = Stack(2)

my_stack.push(1)

my_stack.push(3)
print('---before pop---')
my_stack.print_stack()

print('----poped value---')
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

print('---after pop remaining items---')

my_stack.print_stack()
