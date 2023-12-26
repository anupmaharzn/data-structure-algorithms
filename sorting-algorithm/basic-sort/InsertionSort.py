def insertion_sort(my_list):

    for i in range (1,len(my_list)):
        #front
        temp = my_list[i]
        #back
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    
    return my_list


my_list = [4,2,6,7,1,3]

print(insertion_sort(my_list))