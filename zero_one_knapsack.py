
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print("Maximum value in Knapsack:", knapsack(values, weights, capacity))





















# Defines the knapsack function, which takes:
# values: a list of item values.
# weights: a list of item weights.
# capacity: the maximum weight the knapsack can hold.
# n is the number of items.
# dp: A 2D list (table) initialized to zero, where dp[i][w] represents
# the maximum value we can achieve with the first i items and a knapsack capacity w.
# Loops through each item (i from 1 to n) and each possible weight capacity (w from 1 to capacity).
# If the current item's weight is less than or equal to the current capacity w, it calculates two options:
# Don't include the item: dp[i - 1][w] (value without the item).
# Include the item: values[i - 1] + dp[i - 1][w - weights[i - 1]] (value of the item + maximum value with reduced capacity).
# Takes the maximum of these two options.
# If the item's weight exceeds the current capacity, it cannot be included, so the value remains the same as without the item (dp[i - 1][w]).
# After filling the DP table, dp[n][capacity] holds the maximum value that can be obtained with all items and the given capacity.
# This example solves the knapsack problem with 3 items, values [60, 100, 120], weights [10, 20, 30], and a knapsack capacity of 50. It prints the maximum value that can be carried in the knapsack.