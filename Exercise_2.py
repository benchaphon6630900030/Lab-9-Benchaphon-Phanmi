def Search_binary(array, n):
    low = L = 0  
    high = H = len(array) - 1  
    mid = 0
    
    while L <= H:  
        mid = (H + L) // 2  
        if array[mid] < n:  
            L = mid + 1  
        elif array[mid] > n:  
            H = mid - 1  
        else:  
            return mid  
    return -1
    
array = [7,10,12,14,16,20,29,37]

n_1=int(input("\n""enter number to search for Binary :  "))
n_2=int(input("\n""enter number to search for Binary :  "))

result_array_1 = Search_binary(array,n_1)
result_array_2 = Search_binary(array,n_2)

if result_array_1 != -1:
    print("present at index", str(result_array_1))  
    
    if result_array_2 != -1:
        print("present at index", str(result_array_2))  
   
else:  
    print("is not present in array")
