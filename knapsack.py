class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w / item.weight)
            break
    return finalValue

if __name__ == "__main__":
    print("---- Fractional Knapsack Problem using Greedy Method ----")
    n = int(input("Enter number of items: "))
    arr = []
    for i in range(n):
        profit = float(input(f"Enter profit of item {i+1}: "))
        weight = float(input(f"Enter weight of item {i+1}: "))
        arr.append(Item(profit, weight))
    w = float(input("Enter capacity of knapsack: "))
    print(f"\nMaximum value in knapsack: {fractionalKnapsack(w, arr):.2f}")
