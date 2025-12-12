class LinearSearch:
    def __init__(self):
        self.n = int(input("Enter the number of elements: "))

        self.arr = []
        for i in range(self.n):
            value = int(input(f"Enter element {i + 1}: "))
            self.arr.append(value)

        self.target = int(input("Enter the element to search for: "))

    def search(self):
        for index, value in enumerate(self.arr):
            if value == self.target:
                return index
        return -1

def main():
    ls = LinearSearch()
    result = ls.search()
    if result != -1:
        print(f"Element {ls.target} found at index {result}.")
    else:
        print(f"Element {ls.target} not found in the list.")