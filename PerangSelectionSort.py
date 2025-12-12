import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def selection_sort(arr):
    numArray = len(arr)

    for mainloop in range(numArray - 1):
        min_index = mainloop
        for subloop in range(mainloop + 1, numArray):
            if arr[subloop] < arr[min_index]:
                min_index = subloop
        if min_index != mainloop:
            arr[min_index], arr[mainloop] = arr[mainloop], arr[min_index]
            print(f"{arr[min_index]}, {arr[mainloop]} swapped to {arr[mainloop]}, {arr[min_index]}")
        else:
            print("no swapping")
        print(f"\nPass {mainloop + 1} elements are: {arr}")
        input("\nPress enter key to continue...\n")
    print("Sorted list is:", arr, "\n")       

def main():
    print("\n--- Selection Sort ---\n")
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
    for mainloop in range(n):
        element = int(input(f"Enter element {mainloop + 1}: "))
        arr.append(element)              
    print("\nUnsorted list is:", arr, "\n")
    selection_sort(arr)

if __name__ == "__main__":
    main()           