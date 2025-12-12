import os, PerangLinkList, PerangCircularLinkList

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def list_menu():
    while True:
        clear_screen()
        print("\n--- LinkList Menu ---\n")
        print("1. Dynamic List")
        print("2. Circular List")
        print("3. Return to Main Menu")
        try:
            choice = int(input("\nEnter your choice (1-3): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-3)! not letters or symbols.")
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
            PerangLinkList.main()
        elif choice == 2:
            PerangCircularLinkList.main()
        elif choice == 3:
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
            print("Invalid option!")            