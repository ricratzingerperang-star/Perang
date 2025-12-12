import os

class BinarySearch:
    def __init__(self):
        self.elements = []
    
    def add_element(self, data):
        self.elements.append(data)
        print(f"{data} added to the list")
        input("\nPress Enter key to return to the menu... ")

    def binary_search(self, target):
        sorted_list = sorted(self.elements)

        low, high = 0, len(sorted_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid] == target:
                return mid
            elif sorted_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1              

    def diplay_search_result(self, target):
        index = self.binary_search(target)
        if index != -1:
            print(f"\nElement {target} found at index {index}.\n")
        else:
            print(f"\nElement {target} not found in the list.\n")
        input("\nPress Enter key to return to the menu... ")

    def display(self):
        if len(self.elements) == 0:
            print("\nList is empty!\n")
        else:
            sorted_list = sorted(self.elements)
            print("Sorted list elements are:", *sorted_list)
        input("\nPress Enter key to return to the menu... ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')                  

def main():
    bs = BinarySearch()
    while True:
        clear_screen()
        print("\n--- Binary Search ---\n")
        print("1. Sample # 1: ADD ELEMENT")
        print("2. Sample # 2: SEARCH ELEMENT")
        print("3. Sample # 3: DISPLAY LIST")
        print("4. EXIT")
        try:
            choice = int(input("\nEnter your choice (1-4): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-4)! not letters or symbols.")
            input("\nPress Enter key to refresh...\n")
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
            data = input("Input the element to add to the list: ")
            bs.add_element(data)
        elif choice == 2:
            target = input("Enter the element to search for: ")
            bs.diplay_search_result(target)
        elif choice == 3:
            bs.display()
        elif choice == 4:
            import time
            clear_screen()
            print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
            for _ in range(10):
                print(".", end="", flush=True)
                time.sleep(0.5)
            clear_screen()    
            print("\n\n\n\n\n\n\n\n===== Returned to Searching Menu! =====")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please try again.") 
            input("\nPress Enter key to return to the menu... ")       
if __name__ == "__main__":
    main()                      