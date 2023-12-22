class HashTable:
    #constructor
    #size of a hash table be a prime number because it reduce a collisions
    def __init__(self,size=7):
        #data_map is our hash table(address space and it is a list)
        self.data_map = [None] * size;  #[None,None,...up to size]
    
    #hash method
    def __hash__(self,key):
        #this method return hash-> which is index of our hash table
        my_hash = 0
        for letter in key:
            #k(key) mod n(size of hash table) hash fucntion
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
      # After processing all characters in the key, the final hash value is returned.
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)

    #lets set key-value pair in our hash table
    def set_item(self,key,value):
        #get the index based on key using hash method
        index = self.__hash__(key)
        #initalize empty list in that address(which means index)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.__hash__(key)
        #if not none then we check for that list items
        if self.data_map[index] is not None:

            for i in range(len(self.data_map[index])):

                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        #else return none
        return None 
    
    def keys(self):

        all_keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item('bolts',1400)
my_hash_table.set_item('washers',50)
my_hash_table.set_item('lumber',70)


print(my_hash_table.get_item('bblt')) #none

print(my_hash_table.get_item('washers')) #50


print(my_hash_table.keys()) #['bolts', 'washers', 'lumber']