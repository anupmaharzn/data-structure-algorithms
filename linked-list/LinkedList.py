from Node import *

class LinkedList():
    #constructor of linked list
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

    # append 
    def append(self,value):
        new_node = Node(value)
        
        if self.head is None or self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

        return True

    #pop
    def pop(self):
        # for empty linked list case
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next): #while temp.next is not none
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1

        # for linked list with one node edge case
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp 
    
    #prepend
    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

        return True

    #pop first
    def pop_first(self):

        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        #one node in linked list edge case
        if self.length == 0:
            #coz head is already None
            self.tail = None 

        return temp  #just to see result otherwise return temp obj

    #get method to get node from index
    def get(self,index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp
    
    #set value to change value of node
    def set_value(self,index,value):

        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False

    #insert node in provided index
    def insert(self,index,value):

        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        temp = self.get(index - 1)

        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    # remove node from provided index
    def remove (self,index):

        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length -1:
            return self.pop()
        
        pre = self.get(index - 1)

        temp = pre.next # node to be removed

        pre.next = temp.next

        temp.next = None

        self.length -=1

        return temp

    # reverse linked list

    def reverse(self):
        #switching head and tail pointer
        temp = self.head
        self.head = self.tail
        self.tail = temp
        #main
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after




# #object instantiation
# my_linked_list = LinkedList(4)

# #-------append-----------------#
# my_linked_list.append(2)

# my_linked_list.print_list()

#print('-------pop-----------------')
# # returns 2 node
# print(my_linked_list.pop())
# #returns 4 node
# print (my_linked_list.pop())
# #returns None
# print (my_linked_list.pop())

# print('-----------prepend-------------')

# my_linked_list.prepend(5)

# my_linked_list.print_list()


# print('----------pop first--------------')
# #returns 5
# print(my_linked_list.pop_first())
# #returns 4
# print(my_linked_list.pop_first())
# #returns 2
# print(my_linked_list.pop_first())
# #returns None
# print(my_linked_list.pop_first())

# my_linked_list.print_list()


# print('-----------get node by index--------------')

# my_linked_list = LinkedList(0)

# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)


# print(my_linked_list.get(2))

# print('-----------set value of node by index--------------')
# my_linked_list.set_value(index=1,value=99)

# my_linked_list.print_list()
    

# print('----------insert new node by index---------')

# my_linked_list = LinkedList(0)

# my_linked_list.append(2)

# my_linked_list.insert(1,1)

# my_linked_list.print_list()
    

# print('--------remove node by index--------')

# my_linked_list = LinkedList(11)

# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print(my_linked_list.remove(2),'\n')

# my_linked_list.print_list()


# print('============reverse linked list=========')

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# print('-------before reverse-------')
# my_linked_list.print_list()
# my_linked_list.reverse()
# print('-------after reverse-------')
# my_linked_list.print_list()