def module1():
    while True:
        clear_screen()
        print("\n--- Module 1 ---\nTITLE : Introduction to Data Structure and Python\n")
        print("1. Basic Syntax Example:")
        print("2. Variables and Data Types:")
        print("3. Example of a Python Function:")
        print("4. Return To Main Menu")
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
            sample1()
        elif choice == 2:    
            sample2()
        elif choice == 3:    
            sample3()
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
            print("Ivalid Choice! Try again...")
            input("Press Enter key to return to Module 1...")

def sample1():    
    print("Hello, World!")
    input("Press Enter key to return to Module 1...")


def sample2():
    x = 10 # Integer
    y = 3.14 # Float
    name = "Alice" # String
    is_active = True # Boolean
    print("x = 10 # Integer")
    print("y = 3.14 # Float")
    print("name = 'String'")
    print("is_active = True # Boolean")
    input("Press Enter key to return to Module 1...")

def sample3():    
    def greet(name):
        print(f"Hello, {name}!")
    greet("Alice")
    input("Press Enter key to return to Module 1...")

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')