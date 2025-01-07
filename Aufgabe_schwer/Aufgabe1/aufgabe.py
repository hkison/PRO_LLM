def knapsack(n, W, items):
    # Create a 2D array to store the maximum value at each n and W
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1][0] <= w:
                dp[i][w] = max(items[i-1][1] + dp[i-1][w-items[i-1][0]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

if __name__ == "__main__":
    # Example input
    n = 3
    W = 50
    items = [(10, 60), (20, 100), (30, 120)]

    # Calculate the maximum value
    max_value = knapsack(n, W, items)
    print(max_value)  # Output: 220