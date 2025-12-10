def binary_search(a, low, high, key):
    # low = 0
    # high = 7
    print("\nlow:",low, "high:",high)
    mid = (low + high) // 2  # 7 // 2 = 3
    print(f"low {low} + high {high} = {low + high} // 2 = {mid}")
    print("mid",mid)

    if (low <= high):  
    
        if (a[mid] == key):  
            print("\n(a[mid] == key) mid = ", mid)
            print("index:", mid ," value:",a[mid])
            print("The element is present at index:", mid)  
    
        elif (key < a[mid]): 
            print("\n(key < a[mid]) mid = ", mid) 
            print("Key:", key ,"value:", a[mid])
            binary_search(a, low, mid - 1, key)  
        
        elif (a[mid] < key):  
            print("\n(a[mid] < key) mid = ", mid)
            print("value:", a[mid] ,"Key:", key)
            binary_search(a, mid + 1, high, key)  

    if (low > high):  
        print("Unsuccessful Search")   


a = [6, 12, 14, 18, 22, 39, 55, 182]  

n = len(a)  

low = 0  

high = n - 1  

key = 22  
binary_search(a, low, high, key)  

key = 54  
binary_search(a, low, high, key)  