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
    

    # Breath First Search

    def BFS(self):
        current_node = self.root
        #entire node
        queue = []
        #only value  in result
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results
    
    # Depth First Search

    # DFS PreOrder <NLR>
    def dfs_pre_order(self):
        results = []
        #using recursion
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
             
        traverse(self.root)

        return results
    
    # DFS PostOrder <LRN>

    def dfs_post_order(self):
        results = []
        #using recursion
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    # DFS InOrder <LNR>

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print(my_tree.root.value) #47
# print(my_tree.root.left.value) #21
# print(my_tree.root.right.value) #76


# print(my_tree.contains(27)) #true
# print (my_tree.contains(17)) #false

print('\n-----breath first search----------')

print(my_tree.BFS()) #[47, 21, 76, 18, 27, 52, 82] same order the way we created a tree

print('\n------depth first search----------')

print('\n----DFS-PreOrder---')

print(my_tree.dfs_pre_order())

print('\n----DFS-PostOrder---')

print(my_tree.dfs_post_order())

print('\n----DFS-InOrder---')

print(my_tree.dfs_in_order())