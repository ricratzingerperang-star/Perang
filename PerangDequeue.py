def main(): 
    import os 
    max_size = int(input("Enter the maximum size of the Deque: "))
    deque_arr = [None] * max_size
    right = -1
    left = -1
    # DEQUE with fixed array and None when deleted
    def insert_right():
        global left, right
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        if right == max_size - 1:
            print("Queue is FULL from the right side!")
            return
        try:
            item = int(input("Enter item to insert at right: "))
        except ValueError:
            print("Invalid input!")
            return
        if left == -1:   # empty
            left = 0
            right = 0
        else:
            right += 1
        deque_arr[right] = item
        print(f"{item} inserted at right.")
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        input("\nPress Enter key to return to the menu...")

    def insert_left():
        global left, right
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        if left == 0:
            print("Queue is FULL from the right side!")
            return
        try:
            item = int(input("Enter item to insert at right: "))
        except ValueError:
            print("Invalid input!")
            return
        if left == -1:   # empty
            left = 0
            right = 0
        else:
            left -= 1
        deque_arr[left] = item
        print(f"{item} inserted at right.")
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        input("\nPress Enter key to return to the menu...")
        
    def delete_left():
        global left, right
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        confirm = input(f"Are you sure you want to delete [{deque_arr[left]}] (Y/N): ")
        if confirm.lower() == 'y':
            if left == -1:
                print("Queue is EMPTY! Nothing to delete.")
                return
            removed = deque_arr[left]
            deque_arr[left] = None  # mark as deleted

            print(f"Deleted from left: {removed}")
            if left == right:   # queue becomes empty
                left = -1
                right = -1
            else:
                left += 1
        else:
            print("Deletion has been cancelled!")        
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}") 
        input("\nPress Enter key to return to the menu...")   

    def delete_right():
        global left, right
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        confirm = input(f"Are you sure you want to delete [{deque_arr[right]}] (Y/N): ")
        if confirm.lower() == 'y':
            if right == -1:
                print("Queue is EMPTY! Nothing to delete.")
                return
            removed = deque_arr[right]
            deque_arr[right] = None  # mark as deleted
            print(f"Deleted from right: {removed}")
            if left == right:   # queue becomes empty
                left = -1
                right = -1
            else:
                right -= 1
        else:
            print("Deletion has been cancelled!")        
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")    
        input("\nPress Enter key to return to the menu...")

    def display():
        print(f"Current location of Left index: {left}, Right index: {right}, Queue: {deque_arr}")
        print("Queue:", end=" ")
        for i in range(left, right + 1):
            print(deque_arr[i], end=" ")
        input("\nPress Enter key to return to the menu...")    

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')        

    while True:
        clear_screen()
        print("\n--- INPUT RESTRICTED QUEUE ---\n")
        print("1. Insert at left")
        print("2. Insert at right")
        print("3. Delete from left")
        print("4. Delete from right")
        print("5. Display")
        print("6. Return to Queue Menu")
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
            clear_screen()
            insert_left()
        elif choice == 2:
            clear_screen()
            insert_right()
        elif choice == 3:
            clear_screen()
            delete_left()
        elif choice == 4:
            clear_screen()
            delete_right()
        elif choice == 5:
            clear_screen()
            display()
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
            print("Invalid choice.")
            input("\nPress Enter key to return to the menu...")   