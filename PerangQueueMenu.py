import os, PerangQueue, PerangCircularQueue, PerangDequeue

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("\n--- Queues and Dequeues ---\n")
        print("1. Queue")
        print("2. Dequeue")
        print("3. CircularQueue")
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
            continue
        if choice == 1:
            PerangQueue.main()
        elif choice == 2:
            PerangDequeue.main()
        elif choice == 3:
            PerangCircularQueue.main()
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
            input("\nPress Enter key to return to Queues and Dequeues...")