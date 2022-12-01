def Search_linear(array, n, number):

    for i in range(n):
        if array[i] == number:
            return True
    return False
    
array = [7,10,12,14,16,20,29,37]

n = 8
number_search_1=int(input("\n""enter number to search for Linear :  "))
number_search_2=int(input("\n""enter number to search for Linear :  "))

if Search_linear(array, n, number_search_1):
    print("\n",number_search_1,"is found to number")

    if Search_linear(array, n, number_search_2):
        print("\n",number_search_2,"is found to number")

else:
    print("\n",number_search_1,"is not found to number")
    print("\n",number_search_2,"is not found to number")
