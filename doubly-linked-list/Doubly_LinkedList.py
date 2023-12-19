from Node import *

class DoublyLinkedList:
    #DLL constructor
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    #print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    #append at end
    def append(self,value):
        new_node = Node(value)
        if  self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    #pop from end
    def pop(self):
        # this code is causing error in self.tail.next `cant debug :(`
        # if self.length == 0 or self.head is None:
        #     return None       
        # temp = self.tail
        # self.tail = self.tail.prev # or (temp.prev) same thing
        # #breaking the connection of node
        # self.tail.next = None
        # temp.prev = None
        # self.length -=1
        # if self.length == 0:
        #     self.head = None
        #     self.tail = None
        # return temp

        #--refactored---#
        if self.length == 0:
            return None
        temp = self.tail
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp

    #prepend
    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1

        return True
    
    #pop first
    def pop_first(self):

        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp

    #get node by index
    def get(self,index):

        if index < 0 or index >=self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1 , index,-1):
                temp = temp.prev
        return temp
    
    #change value of node by index
    def set_value(self,index,value):
        temp = self.get(index)
        if temp: #true if temp is not none
            temp.value = value
            return True
        return False
    
    #insert 
    def insert(self,index,value):

        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        #main 
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length +=1
        return True        
    #remove
    def remove(self):
        #left to do
        None

    #remove
    def remove(self,index):

        if index <0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        #main
        before.next = temp.next # or simple after
        after.prev = temp.prev  # or simple before
        temp.next = None
        temp.prev = None

        # #alternative main
        # temp.next.prev = temp.prev
        # temp.prev.next = temp.next
        # temp.next = None
        # temp.prev = None

        self.length -=1
        return temp


# my_doubly_linked_list = DoublyLinkedList(7)

# print('------------append at end----------')
# my_doubly_linked_list.append(77)
# my_doubly_linked_list.append(78)

# my_doubly_linked_list.print_list()

# print('------------pop from end----------')
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())


# print('--------doubly linked list before prepend-----')
# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(3)


# my_doubly_linked_list.print_list()

# print('--------prepend at begining-----')
# my_doubly_linked_list.prepend(1)

# my_doubly_linked_list.print_list()



# print('----doubly linked list before pop first------')
    
# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(1)

# my_doubly_linked_list.print_list()


# print('---pop first ---')

# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())


# print('-------------get node by index----------------')

# my_doubly_linked_list = DoublyLinkedList(0)

# my_doubly_linked_list.append(1)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)

# print(my_doubly_linked_list.get(1))
# print(my_doubly_linked_list.get(2))
#-------------------------------------------------------------------------
        
# print('--------chnage value of node by index------')

# my_doubly_linked_list = DoublyLinkedList(11)

# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(23)
# my_doubly_linked_list.append(7)
# print('---before changing the node value----')
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.set_value(1,99)

# print('---after changing the 1 index node value---')

# my_doubly_linked_list.print_list()
        
#---------------------------------------------------------------------------
        
# print('------insert by index-----------')

# my_doubly_linked_list = DoublyLinkedList(1)

# my_doubly_linked_list.append(3)

# my_doubly_linked_list.print_list()

# print('----insert at 1st index---')

# my_doubly_linked_list.insert(1,2)

# my_doubly_linked_list.print_list()


#--------------------------------------------------------------------
    
print ('-------remove node by index------')

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()

print('-after removing node by index 1--')

my_doubly_linked_list.remove(1)

my_doubly_linked_list.print_list()
