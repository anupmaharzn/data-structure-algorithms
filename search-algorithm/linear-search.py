def linear_search(arr,target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i #target found, return the index
    
    return -1 # target not found


my_list = [12,23,34,121,3,4321]


target_element = 3

result = linear_search(my_list,target_element)


if result != -1:
    print(f'element {target_element} found at index {result}')
else:
    print(f'element {target_element} not found in the list')