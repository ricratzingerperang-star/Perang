import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def sort(arr):
    n = len(arr)
    print("\nUnsorted list is: ")
    print(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key 
    print("\nSorted list is:")
    print(arr) 
    import time
    clear_screen()
    print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
    for _ in range(10):
        print(".", end="", flush=True)
        time.sleep(0.5)
    clear_screen()
    print("\n\n\n\n\n\n\n\n===== Returned to Sorting Menu! =====")
    time.sleep(2)   

def main():
    print("\n--- Insertion Sort ---\n")
    try:
        n = int(input("Enter Number Of Elements: --> "))
    except ValueError:
        print("\nPlease enter a valid number! not letters or symbols.")
        input("\nPress Enter key to return to the Sorting Menu...")
        import time
        clear_screen()
        print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(0.5)
        clear_screen()
        print("\n\n\n\n\n\n\n\n===== Returned to Sorting Menu! =====")
        time.sleep(2)    
        return

    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    sort(arr)   
    
if __name__ == "__main__":
    main()          