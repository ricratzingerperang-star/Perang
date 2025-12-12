import os
MAX_SIZE = 5
queue_arr = [None] * MAX_SIZE
front = -1
rear = -1
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enqueue():
    global front, rear
    if rear == MAX_SIZE - 1:
        print("Queue is full")
    else:
        add_item = input("\nEnter element to be inserted: ")
        if front == -1:
            front = 0
        rear += 1
        queue_arr[rear] = add_item
        print(f"Element '{add_item}' has been inserted")
    print(f"front: {front}, rear: {rear}, Queue: {queue_arr}")
    input("\nPress Enter key to return to the menu...")

def dequeue():
    global rear, front
    if front == -1 or front > rear:
        print("\nThe Queue Underflow!")
    else:
        confirm = input(f"\nThe item to be deleted is '{queue_arr[front]}'\nAre you sure you want to delete this item? (Y/N): ")
        if confirm.lower() == 'y':
            print(f"\nThe deleted element is: '{queue_arr[front]}'.")
            queue_arr[front] = None
            front += 1
            if front > rear:
                front = -1
                print("\nThe Queue is now Empty!")
        else:
            print("\nDeletion has been cancelled.")
    print(f"front: {front}, rear: {rear}, queue_arr: {queue_arr}")
    input("\nPress Enter key to return to the menu...")

def traverse():
    if front == -1:
        print("\nThe Queue is Empty!")
        print(f"front: {front}, rear: {rear}, Queue: {queue_arr}")
    else:
        print(f"front: {front}, rear: {rear}, Queue: {queue_arr}")
        print("\nThe element(s) in the Queue are:", end=" ")
        for i in range(rear + 1):
            print(queue_arr[i],end=" ")
    input("\nPress Enter key to return to the menu...")

def main():
    while True:
        clear_screen()
        print("\n--- Queue using Array ---\n")
        print('1. ENQUEUE')
        print("2. DEQUEUE")
        print("3. TRAVERSE")
        print("4. Return to Queue Menu")
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
            clear_screen()
            enqueue()
        elif choice == 2:
            clear_screen()
            dequeue()
        elif choice == 3:
            clear_screen()
            traverse()
        elif choice == 4:
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()    
            print("\n\n\n\n\n\n\n\n\n===== Returned to Queue Menu! =====")
            time.sleep(2)
            break
        else:
            print("Invalid Choice. Please try again.")
            input("\nPress Enter key to return to the menu...")

if __name__ == "__main__":
    main()