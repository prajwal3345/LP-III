# Write a program to solve a fractional Knapsack problem using a greedy method.

def fractional_knapsack(values, weights, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print("Maximum value in Knapsack:", fractional_knapsack(values, weights, capacity))




# This defines a function fractional_knapsack that takes three inputs:
# values: a list of values for each item.
# weights: a list of weights corresponding to each item.
# capacity: the maximum weight the knapsack can hold.
# zip(values, weights) pairs each value with its corresponding weight.
# sorted(..., key=lambda x: x[0] / x[1], reverse=True): 
# Sorts items by their value-to-weight ratio in descending order, making items with the highest ratio come first.
# Initializes total_value to store the maximum value accumulated in the knapsack.
# Iterates over each item in the sorted items list, where value is the item’s value, and weight is the item’s weight.
# Checks if the remaining capacity can hold the entire weight of the current item.
# If true, it adds the full value of this item to total_value and reduces the capacity by the item’s weight.
# If the item’s weight exceeds the remaining capacity, only a fraction of the item is added:
# value * (capacity / weight) calculates the partial value that can fit.
# break ends the loop because the knapsack is now full.
# Returns the total maximum value the knapsack can hold.
# Example input where values and weights are lists representing items, and capacity is the knapsack limit.
# The function is called, and it prints the maximum value obtainable.