import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class CircularList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def __getitem__(self, index):
        if not self.data:
            raise IndexError("Circular list is empty.")
        return self.data[index % len(self.data)]  # circular behavior

    def __str__(self):
        if not self.data:
            return "Circular List is empty"
        return " -> ".join(str(x) for x in self.data) + " -> (loops)"

cl = CircularList()
def main():
    try:
        n = int(input("\nEnter Number Of Elements: --> "))
    except ValueError:
        print("\nPlease enter a valid number! not letters or symbols.")
        input("\nPress Enter key to return to the Main Menu...\n")
        import time
        clear_screen()
        print("\n\n\n\n\n\n\n\nReturning", end="", flush=True)
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(0.5)
        clear_screen()
        print("\n\n\n\n\n\n\n\n===== Returned to Main Menu! =====")
        time.sleep(2)
        return

    for i in range(n):
        val = input(f"Enter value {i+1}: ")
        cl.add(val)

    print("\nYour Circular List:")
    print(cl)

    while True:
        idx = input("\nEnter index to access (negative OK, type exit to exit): ")
        if idx == "exit":
            break
        print(f"Element at index {idx} =", cl[idx])
