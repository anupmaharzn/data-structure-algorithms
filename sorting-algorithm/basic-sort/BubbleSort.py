def BubbleSort(my_list):

    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

my_list = [4,2,6,5,1,3]

print(BubbleSort(my_list))