import os, PerangSorting, PerangSelectionSort, PerangBubbleSort

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Sorting():
    while True:
        clear_screen()
        print("\n--- Sorting Techniques ---\n")
        print("1. Sorting")
        print("2. Selection Sort")
        print("3. Bubble Sort")
        print("4. Return to Main Menu")
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
            PerangSorting.main()
        elif choice == 2:    
            PerangSelectionSort.main()
        elif choice == 3:
            PerangBubbleSort.main()    
        elif choice == 4:
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()    
            print("\n\n\n\n\n\n\n\n===== Returned to Main Menu! =====")
            time.sleep(2)
            break
        else:
            print("Invalid Choice! Try again...")
            input("\nPress Enter key to return to Sort Menu...")