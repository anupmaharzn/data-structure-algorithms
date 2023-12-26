

#merge helper function to combine 2 sorted list
def merge(list1,list2):
    combined = []
    i=0
    j=0
    #both present case
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    #first left case
    while i< len(list1):
        combined.append(list1[i])
        i +=1
    #second left case
    while j < len(list2):
        combined.append(list2[j])
        j +=1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index]) #upto but not including
    right = merge_sort(my_list[mid_index:])

    return merge(left,right)



original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)


print('original list:',original_list)
print('\nsorted list: ',sorted_list)
