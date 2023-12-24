from Node import Node

class RecusiveBST:

    def __init__(self):
        self.root = None


    #insert in recursive way
    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node

    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)

    
    #contains in recursive way 
    #private method
    def __r_contains(self,current_node,value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left,value)
        if value > current_node.value:
            return self.__r_contains(current_node.right , value)
        
    

    #public method
    def r_contains(self,value):
        return self.__r_contains(self.root,value)


    #min value in tree from given node 
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    #delete node (recursive way)
    def __delete_node(self,current_node,value):
        #indicates the node we try to delete not exist in tree
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right,value)
        else:
            #deleting leaf node
            if current_node.left == None and current_node.right == None: #means leaf node
                return None
            #deleting node case when open on left but node on right (only right subtree)
            elif current_node.left ==None: #means has only right subtree
                current_node = current_node.right
            #deleting node case when open on right but node on left (only left subtree)
            elif current_node.right == None:
                current_node = current_node.left
            #deleting node case when both side have nodes (both left and right subtree)
            else:
                #find the min value
                sub_tree_min = self.min_value(current_node.right)
                #change the value of current node(node to remove) with min value (now 2 node with same value)
                current_node.value = sub_tree_min
                #delete the second node which is from right subtree 
                current_node.right = self.__delete_node(current_node.right,sub_tree_min)
                
        return current_node
    
    def delete_node(self,value):
        self.__delete_node(self.root,value)



my_tree = RecusiveBST()

my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)




print('Root:',my_tree.root.value)
print('Root -> Left',my_tree.root.left.value)
print('Root -> Right',my_tree.root.right.value)


# print(my_tree.min_value(my_tree.root))

# print(my_tree.r_contains(3))
# print(my_tree.r_contains(4))


print('---delete node---')

my_tree.delete_node(2)

print('Root:',my_tree.root.value)
print('Root -> Left',my_tree.root.left.value)
print('Root -> Right',my_tree.root.right)
