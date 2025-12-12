import os
MAXSIZE = 5
top = -1
stack = [0] * MAXSIZE
   
def push():
    global top
    # If the stack is full, print an error message
    print("\nPUSH in STACK\n")
    if top == MAXSIZE - 1:
        print("The Stack is Full!")
    else:
        # Increment top and insert the element
        item = input("Enter the element to be inserted: ")
        top += 1
        stack[top] = item
        print(f"Element '{item}' has been inserted")
    input("\nPress Enter key to return to Module 3...")

def pop():
    global top
    # If the stack is empty, print an error message
    print("\nPOP in STACK\n")
    if top == -1:
        print("The Stack is Empty!")
    else:
        # Pop the top element and decrement top
        item = stack[top]
        confirm = input(f"The item to be deleted is '{item}'.\n\nAre you sure you want to delete this item? (Y/N): ")
        if confirm.lower() == 'y':
            top -= 1
            print(f"The deleted element is: '{item}'.")
        else:
            print("Deletion has been cancelled.")
    input("\nPress Enter key to return to Module 3...")

def traverse():
    # If the stack is empty, print an error message
    print("\nTRAVERSE in STACK\n")
    if top == -1:
        print("The Stack is Empty!")
    else:
        print("The element(s) in the Stack are:")
        for i in range(top, -1, -1):
            print(stack[i], end = " ")
    input("\n\nPress Enter key to return to Module 3...")    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def module3():
    global top
    while True:
        clear_screen()
        print("\n--- Module 3 ---\nTITLE : The Stack")
        print("STACK using Array\n")
        print("1. Sample # 1: PUSH")
        print("2. Sample # 2: POP")
        print("3. Sample # 3: TRAVERSE")
        print("4. RETURN TO MAIN")
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
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            traverse()
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
            print("\nInvalid Choice. Please try again.")
            input("\nPress Enter key to return to Module 3...")