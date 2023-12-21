def binary_search (arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2 # ?// this operator floor the division
        mid_element = arr[mid]
        if mid_element == target:
            return mid # targe found , return the index
        elif mid_element < target:
            low = mid + 1 #adjust the search range
        else:
            high = mid -1 #adjust the search range

    return -1 #target not found

my_sorted_list = [1,3,4,5,7,9,11,13]

target_element = 7 

result = binary_search(my_sorted_list,target_element)


if result != -1:
    print(f'element {target_element} found at index {result}')

else:
    print(f'element {target_element} not found in the list')