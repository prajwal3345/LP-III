# Write a program for analysis of quick sort by using deterministic and randomized variant.


import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Randomly choosing a pivot
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Function to analyze the performance
def analyze_sorting(n):
    arr = [random.randint(0, 10000) for _ in range(n)]
    
    # Analyze deterministic quick sort
    start_time = time.time()
    deterministic_quick_sort(arr.copy())
    deterministic_time = time.time() - start_time
    
    # Analyze randomized quick sort
    start_time = time.time()
    randomized_quick_sort(arr.copy())
    randomized_time = time.time() - start_time
    
    print(f"Array size: {n}")
    print(f"Deterministic Quick Sort Time: {deterministic_time:.6f} seconds")
    print(f"Randomized Quick Sort Time: {randomized_time:.6f} seconds")

# Example usage
if __name__ == "__main__":
    analyze_sorting(1000)  # Change the size of the array as needed





# Deterministic Quick Sort:

# This function (deterministic_quick_sort) recursively sorts an array by:
# Choosing the middle element as the pivot.
# Creating three sublists: left (elements smaller than the pivot), middle (elements equal to the pivot), and right (elements greater than the pivot).
# Recursively applying the same sorting logic to the left and right sublists, and concatenating them.
# Randomized Quick Sort:

# This function (randomized_quick_sort) works similarly to the deterministic version, but:
# It randomly selects a pivot index in the array instead of always choosing the middle element.
# This randomness helps avoid worst-case scenarios (e.g., when the array is already sorted or nearly sorted).
# Performance Analysis:

# The analyze_sorting function:
# Generates a random array of size n.
# Times the execution of both deterministic and randomized quicksort by copying the array for each sort to avoid modifying the original array.
# Prints the time taken for each sorting algorithm to process the array.
# Example Usage:

# In the if __name__ == "__main__": block, the analyze_sorting function is called with n = 1000 to test the performance for sorting an array of 1000 random integers.
# The times taken by both sorting algorithms (deterministic and randomized) are printed.
# The program will print the time taken by each sorting algorithm (deterministic vs. randomized) to sort an array of 1000 elements.