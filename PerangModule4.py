import os
max_size = 3
rear = -1
front = -1
queue_arr = [None] * max_size
def enqueue():
    global rear, front
    if rear == max_size - 1:
        print("\nQueue overflow!")
    else:
        add_item = int(input("\nInput the element for the queue: "))
        if front == -1:
            front = 0
        rear += 1
        queue_arr[rear] = add_item
        print(f"\nElement '{add_item}' has been queued")
    input("\nPress Enter key to return to Module 4...")

def dequeue():
    global rear, front
    if front == -1 or front > rear:
        print("\nQueue underflow!")
    else:
        print(f"\nThe item to be dequeued is '{queue_arr[front]}'.")
        confirm = input("Are you sure you want to delete this item? (Y/N): ")
        if confirm.lower() == 'y':
            print(f"The deleted element is: '{queue_arr[front]}'.")
            front += 1
            if front > rear:
                front = rear = -1
        else:
            print("Deletion has been cancelled.")
    input("\nPress Enter key to return to Module 4...")

def traverse():
    if front == -1 or front > rear:
        print("\nQueue is empty!")
    else:
        print("\nQueue elements are:", end=" ")
        for i in range(front, rear + 1):
            print(queue_arr[i], end=" ")
        print()
    input("\nPress Enter key to return to Module 4...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def module4():
    while True:
        clear_screen()
        print("\n--- Module 4 ---\nTITLE : Queues and Dequeues")
        print("QUEUE using Array\n")
        print("1. Sample # 1: ENQUEUE")
        print("2. Sample # 2: DEQUEUE")
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
            enqueue()
        elif choice == 2:
            dequeue()
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
            input("\nPress Enter key to return to Module 4...")         