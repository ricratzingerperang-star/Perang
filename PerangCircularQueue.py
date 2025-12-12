import os

max_size = 5
deque_arr = [None] * max_size
rear = -1
front = -1

def insert_rear():
    global rear, front
    if (rear + 1) % max_size == front:
        print("\nDeque overflow!\n")
        print(rear)
    else:
        add_item = int(input("\nInput the element for the deque at the rear: "))
        if front == -1:
            front = 0
        rear = (rear + 1) % max_size
        deque_arr[rear] = add_item
        print(f"\nElement {add_item} added at the rear.\n")
    input("Press Enter key to return to the manu...")   

def insert_front():
    global rear, front
    if (rear + 1) % max_size == front:
        print("\nDequeue overflow!\n")
    else:
        add_item = int(input("Input the element for the deque at the front: "))
        if front == -1:                 
            front = rear = 0
        else:
            front = (front - 1 + max_size) % max_size
        deque_arr[front] = add_item
        print(f"Element {add_item} added at the front.\n")
    input("Press Enter key to return to the manu...")

def delete_front():
    global rear, front
    if front == -1:
        print("\nDeque underflow!\n")
    else:
        print("\nElement deleted from the front is: ",deque_arr[front])  
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % max_size
    input("Press Enter key to return to the manu...")

def delete_rear():
    global rear, front
    if front == -1:
        print("\nDeque underflow\n")
    else:
        print("Element deleted from the rear is:", deque_arr[rear]) 
        if front == rear:
            front = rear = -1
        else:
            rear = (rear - 1 + max_size) % max_size
    input("Press Enter key to return to the manu...")

def traverse():
    if front == -1:
        print("\nDeque is empty!\n")
    else:
        print("\nDeue elements are:", end=" ")
        i = front
        while i != rear:
            print(deque_arr[i], end=" ")
            i = (i + 1) % max_size
        print(deque_arr[i])
    input("Press Enter key to return to the manu...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  

def main():
    while True:
        clear_screen()
        print("\n--- Dequeue Using Array ---\n")
        print("1. Insert at Rear")         
        print("2. Insert at Front")
        print("3. Delete from Rear")
        print("4. Delete from Front")
        print("5. Traverse")
        print("6. Exit")
        try:
            choice = int(input("\nEnter your choice (1-6): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-6)! not letters or symbols.")
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
            insert_rear()
        elif choice == 2:
            insert_front()
        elif choice == 3:
            delete_rear()
        elif choice == 4:
            delete_front()
        elif choice == 5:
            traverse()
        elif choice == 6:
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()    
            print("\n\n\n\n\n\n\n\n===== Returned to Queue Menu! =====")
            time.sleep(2)
            break
        else:
            print("Invalid Choice. Please try again.")
            input("Press Enter key to return to the manu...")

if __name__ == "main":
    main()