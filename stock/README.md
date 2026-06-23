# Best Time to Buy and Sell Stock

**Platform:** LeetCode 121  
**Difficulty:** Easy  
**Topic:** Arrays, Greedy

---

## Problem Description

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit you can achieve by buying on one day and selling on a later day.

Return `0` if no profit is possible.

**Example:**
```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price=1), sell on day 5 (price=6). Profit = 6 - 1 = 5.
```

---

## Approach — Single Pass (Greedy)

The key insight is that to maximize profit at any point, you want to have bought at the **lowest price seen so far**.

As we scan left to right:
1. Calculate profit if we sell today: `prices[i] - minimum`
2. Update the running minimum
3. Track the best profit seen so far

This eliminates the need for a nested loop — we only need one pass.

```python
class Solution():
    def max_profit(self, prices):
        curr = 0
        profit = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - minimum
            minimum = min(minimum, prices[i])
            curr = max(curr, profit)
        return curr

def main():
    prices = list(map(int, input("Enter the stock prices: ").split()))
    s = Solution()
    max_profit = s.max_profit(prices)
    print("The maximum profit is", max_profit)

if __name__ == "__main__":
    main()
```

---

## Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | Single pass through the array |
| **Space** | O(1) | Only three variables used regardless of input size |

---

## Key Takeaway

The brute force O(n²) approach checks every pair (buy, sell). The greedy insight reduces this to O(n) by recognising that you only ever need to track the minimum price seen so far — there is no need to look back further than that.