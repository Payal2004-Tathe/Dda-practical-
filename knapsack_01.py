# 0/1 Knapsack Problem using Dynamic Programming (Dynamic Input)

def knapsack_01(n, values, weights, W):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace selected items
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    selected_items.reverse()
    return dp[n][W], selected_items


if __name__ == "__main__":
    print("---- 0/1 Knapsack Problem using Dynamic Programming ----")
    n = int(input("Enter number of items: "))
    values = []
    weights = []

    for i in range(n):
        val = int(input(f"Enter value (profit) of item {i + 1}: "))
        wt = int(input(f"Enter weight of item {i + 1}: "))
        values.append(val)
        weights.append(wt)

    W = int(input("Enter maximum capacity of knapsack: "))

    max_value, selected_items = knapsack_01(n, values, weights, W)

    print(f"\nMaximum value that can be obtained: {max_value}")
    print("Items included (0-based indices):", selected_items)
