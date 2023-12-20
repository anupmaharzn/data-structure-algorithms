from Node import *

class BinarySearchTree:

    def __init__(self):
        self.root = None

    #INSERT 
    
    def insert(self,value):
        new_node = Node(value)
        # for to check is tree is empty then just insert new_node
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            #for duplicate node insertion edge case
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # if there is node then move pointer to that node
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                # if there is node then move pointer to that node
                temp = temp.right
            
    # check if value contains in tree or not
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.value) #47
print(my_tree.root.left.value) #21
print(my_tree.root.right.value) #76


print(my_tree.contains(27)) #true
print (my_tree.contains(17)) #false

