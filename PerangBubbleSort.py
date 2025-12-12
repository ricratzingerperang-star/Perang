import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bubble_sort(arr):
    numArray = len(arr)
    for mainloop in range(numArray - 1):
        xchanges = 0
        print(f"Pass {mainloop} Element: {arr}\n")
        for subloop in range(numArray - 1 - mainloop):
            if arr[subloop] > arr[subloop + 1]:
                arr[subloop + 1], arr[subloop] = arr[subloop], arr[subloop + 1]
                xchanges += 1
                print(f"Elements are: {arr}")
            else:
                print("No Swapping")
            print(f"\nPass {mainloop + 1} elements are: \n{arr}")
        input("\nPress enter key to continue... ")
        clear_screen()
        print()
        if xchanges == 0:
            break

    clear_screen()
    print("BUBBLE SORT\n")
    print("Sorted list is/are:", arr, "\n")

def add_element():
    print("---Bubble Sort---\n")
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    print("\nUnsorted list is:", arr, "\n")
    return arr
    

def display_elements(arr):
    print("\nCurrent elements in the list:")
    print(" index, Element")
    for i, val in enumerate(arr):
        print(f"  [{i}] -> {val}")
    print()  # blank line
    

def main():
    arr = []
    while True:
        clear_screen()
        print("\n--- Bubble Sort Menu ---\n")
        print("1. Add Element")
        print("2. Display Elements")
        print("3. Sort Elements")
        print("4. Return to Sorting Menu")
        try:
            choice = int(input("\nEnter your choice (1-4): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-4)! not letters or symbols.")
            input("\nPress Enter key to refresh...")
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nRefreshing", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()
            print("\n\n\n\n\n\n\n\n===== Refreshed! =====")
            time.sleep(2)
            continue

        if choice == 1:
            arr = add_element()
            input("\nPress enter key to continue... ")
        elif choice == 2:
            if arr:
                display_elements(arr)
            else:
                print("No elements to display. Please add elements first.")
            input("\nPress enter key to continue... ")    
        elif choice == 3:
            if arr:
                bubble_sort(arr)
            else:
                print("No elements to sort. Please add elements first.")
            input("\nPress enter key to continue... ")    
        elif choice == 4:
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()
            print("\n\n\n\n\n\n\n\n===== Returned to Sorting Menu! =====")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Try again.")
            input("\nPress enter key to continue... ")

if __name__ == "__main__":
    main()