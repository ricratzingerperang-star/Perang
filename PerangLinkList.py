import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class DynamicList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)

    def __str__(self):
        return " -> ".join(str(x) for x in self.data)


dl = DynamicList()
def main():
    while True:
        clear_screen()
        print("\n--- Dynamic List Menu ---\n")
        print("1. Add")
        print("2. Insert at index")
        print("3. Delete value")
        print("4. Display list")
        print("5. Return to List Menu")
        try:
            choice = int(input("\nEnter your choice (1-5): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-5)! not letters or symbols.")
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
            val = input("Enter value to add: ")
            dl.add(val)
        elif choice == 2:
            index = int(input("Enter index: "))
            val = input("Enter value: ")
            dl.insert(index, val)
        elif choice == 3:
            val = input("Enter value to delete: ")
            dl.delete(val)
        elif choice == 4:
            print("\nList:", dl)
        elif choice == 5:
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()    
            print("\n\n\n\n\n\n\n\n===== Returned to List Menu! =====")
            time.sleep(2)
            break
        else:
            print("Invalid option!")
