import os

class SequentialSearch:
    def __init__(self):
        self.elements = []

    def add_element(self, data):
        self.elements.append(data)
        print(f"{data} added to the list")

    def search(self, target):
        found = False
        for index, element in enumerate(self.elements):
            if element == target:
                found = True
                break
        return found, index if found else -1

    def diplay_search_result(self, target):
        found, index = self.search(target)
        if found:
            print(f"\nElement {target} found at index {index}.\n")
        else:
            print(f"Element {target} not found n the list.\n")
        input("\nPress Enter key to return to the menu...")

    def display(self):
        if len(self.elements) == 0:
            print("\nList is empty!\n") 
        else:
            print("List elements are:", end=" ")
            for element in self.elements:
                print(element, end=" ")
            print()
        input("\nPress Enter key to return to the menu...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    sequential_search = SequentialSearch()
    while True:
        clear_screen()
        print("--- Sequential Search ---")
        print("1. Add Element")
        print("2. Search Element") 
        print("3. Display List") 
        print("4. Return to Searching Menu")        
        try:
            choice = int(input("\nEnter your choice (1-3): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-3)! not letters or symbols.")
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
            num_elements = int(input("Enter the number of elements to add"))
            for i in range(num_elements):
                data = int(input("Input the element to add to the list: "))
                sequential_search.add_element(data)
        elif choice == 2:
            target = int(input("Enter the element to search for: "))
            sequential_search.diplay_search_result(target)
        elif choice == 3:
            sequential_search.display()      
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
            print("Invalid Choice. Please Try Again.")
            input("\nPress Enter key to return to the menu...")