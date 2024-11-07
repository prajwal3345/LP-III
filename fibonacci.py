# Write a program non-recursive and recursive program to calculate Fibonacci numbers and
# analyze their time and space complexity.

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    n = int(input("Enter the term for Fibonacci: "))
    choice = int(input("Choose method (1 for Iterative, 2 for Recursive): "))

    if choice == 1:
        print(f"Fibonacci (Iterative) of {n} is: {fibonacci_iterative(n)}")
    elif choice == 2:
        print(f"Fibonacci (Recursive) of {n} is: {fibonacci_recursive(n)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


# def fibonacci_iterative(n): This defines a function called fibonacci_iterative that takes an integer n as input.

# if n <= 1: return n: Checks if n is 0 or 1. If so, it simply returns n since the Fibonacci number of 0 is 0 and of 1 is 1.

# a, b = 0, 1: Initializes two variables, a and b, with the values 0 and 1, representing the first two Fibonacci numbers.

# for _ in range(2, n + 1): Starts a loop from 2 up to n to calculate the Fibonacci numbers iteratively.

# a, b = b, a + b: Updates a and b so that b takes on the value of the next Fibonacci number, and a takes on the previous value of b.

# return b: After the loop, b holds the Fibonacci number for the term n, which is returned.

# def fibonacci_recursive(n): This defines a function called fibonacci_recursive that also takes an integer n.

# if n <= 1: return n: Checks if n is 0 or 1 and returns n directly, as these are the base cases.

# return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2): If n is greater than 1, it calls fibonacci_recursive for n - 1 and n - 2 and adds the results. 
# This follows the Fibonacci formula recursively until it reaches the base cases.

# def main(): Defines a function called main that handles user interaction and calls the appropriate Fibonacci calculation method.

# n = int(input("Enter the term for Fibonacci: ")): Prompts the user to enter the term n for which they want the Fibonacci number, and converts this input to an integer.

# choice = int(input("Choose method (1 for Iterative, 2 for Recursive): ")): Prompts the user to choose between the iterative (1) or recursive (2) method.

# if choice == 1: Checks if the user selected the iterative method.

# print(f"Fibonacci (Iterative) of {n} is: {fibonacci_iterative(n)}): If so, it calls fibonacci_iterative(n) and prints the result.
      
# elif choice == 2: Checks if the user selected the recursive method.
      
# print(f"Fibonacci (Recursive) of {n} is: {fibonacci_recursive(n)}): If so, it calls fibonacci_recursive(n) and prints the result.

# else: print("Invalid choice."): If the user input is not 1 or 2, it prints "Invalid choice."