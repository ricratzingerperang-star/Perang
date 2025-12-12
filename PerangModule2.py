def module2():
    while True:
        clear_screen()
        print("\n--- Module 2 ---\nTITLE : Arrays\n")
        print("1. Sample # 1: Basic Array structure")
        print("2. Sample # 2: Create an array using loop")
        print("3. Sample # 3: Using Arrays in calculation")
        print("4. Sample # 4: Inputted number of elements in an array")
        print("5. Sample # 5: inputted values of the elements")
        print("6. Sample # 6: Multi-dimensional array")
        print("7. Sample # 7: Printed Multi-Dimensional Array")
        print("8. Sample # 8: Array inside a function")
        print("9. Return to Main Menu")
        try:
            choice = int(input("\nEnter your choice (1-9): --> "))
        except ValueError:
            print("\nPlease enter a valid number from (1-9)! not letters or symbols.")
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
            sample1()
        elif choice == 2:    
            sample2()
        elif choice == 3:
            sample3()
        elif choice == 4:    
            sample4()
        elif choice == 5:    
            sample5()
        elif choice == 6:    
            sample6()
        elif choice == 7:    
            sample7()
        elif choice == 8:    
            sample8()
        elif choice == 9:    
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
            print("Ivalid Choice! Try again...")

def sample1():
    if __name__ == "__main__":
        sample_array = ["A", "L", "E", "X"]
        print(sample_array[0])
        another_array = [1, 2, 3, 12, 99]
        print(another_array[0])
    print("Press Enter key to return to Module 2...")


def sample2():        
    if __name__ == "__main__":
        sample_array = [88] * 9
        print("Element - Value")
        for x in range(9):
            print(f"{x} ------ {sample_array[x]}")
    print("Press Enter key to return to Module 2...")

def sample3():        
    if __name__ == "__main__":
        another_array = [4, 12, 30, 10, 25]
        sum_result = 0
        total = 0
        for x in range(5):
            print(another_array[x], end=" ")
            sum_result = another_array[x]
            total += sum_result
        print(f"The sum is: {total}")
        print("TY :)")
    print("Press Enter key to return to Module 2...")

def sample4():        
    if __name__ == "__main__":
        elements = int(input("Enter number of elements: "))
        sample_array = [88] * elements
        print("Element - Value")
        for x in range(elements):
            print(f"{x} ------ {sample_array[x]}")
    print("Press Enter key to return to Module 2...")

def sample5():            
    if __name__ == "__main__":
        elements = int(input("Enter number of elements: "))
        sample_array = []
        for x in range(elements):
            num = int(input(f"Enter element no. {x}: "))
            sample_array.append(num)
        for y in range(elements):
            print(sample_array[y], end=" ")
        print() # Print a newline for better formatting
    print("Press Enter key to return to Module 2...")

def sample6():        
    if __name__ == "__main__":
        multi_array = [[2, 3, 4],
                      [6, 7, 8]]
        print(multi_array[1][2])
    print("Press Enter key to return to Module 2...")

def sample7():    
    if __name__ == "__main__":
        multi_array = [[2, 3, 4],
                      [6, 7, 8]]
        for row in range(2):
            for column in range(3):
                print(multi_array[row][column], end=" ")
        print() # Print a newline for each row
    print("Press Enter key to return to Module 2...")

def sample8():        
    def first_function():
        integer_array = [1, 2, 3, 4, 5]
        print(integer_array[2])
        string_array = ["A", "B", "C", "D"]
        print(string_array[2])
    def main():
        first_function()
    if __name__ == "__main__":
        main()
    print("Press Enter key to return to Module 2...")

def clear_screen():    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')