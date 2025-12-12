import os, PerangModule1, PerangModule2, PerangModule3, PerangQueueMenu, PerangSortMenu, PerangSearchingMenu, PerangListMenu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Main_Menu():
    while True:
        clear_screen()
        print("\n=== DATA STRUCTURE'S === \n     AND ALGORITHM\n")
        print("1. MODULE # 1:  Introduction to Data Structure and Python")
        print("2. MODULE # 2:  Arrays")
        print("3. MODULE # 3:  The Stack")
        print("4. MODULE # 4:  Queues and Dequeues")
        print("5. MODULE # 5:  Sorting Techniques")
        print("6. MODULE # 6:  Link List")
        print("7. MODULE # 7:  Searching")
        print("8. Exit")
        try:
            choice = int(input("\nEnter your choice (1-8): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-8)! not letters or symbols.")
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
            PerangModule1.module1()
        elif choice == 2:
            PerangModule2.module2()
        elif choice == 3:    
            PerangModule3.module3()
        elif choice == 4:    
            PerangQueueMenu.main()
        elif choice == 5:
            PerangSortMenu.Sorting()
        elif choice == 6:
            PerangListMenu.list_menu()    
        elif choice == 7:
            PerangSearchingMenu.Searching()
        elif choice == 8:    
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nExiting", end="", flush=True)
            for _ in range(15):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()
            print("\n\n\n\n\n\n\n\nExited! Thank you for using me. Goodbye :)")
            break
        else:
            print("\nInvalid choice! Try again...")
         
if __name__ == "__main__":
    Main_Menu()          
            