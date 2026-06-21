# Maximum Ice Cream Bars

## Problem Description

A boy wants to buy ice cream bars on a hot summer day. There are `n` bars available,
given as an array `costs` where `costs[i]` is the price of the `i`-th bar. The boy
starts with a fixed number of `coins` and wants to buy as many bars as possible,
in any order he likes.

**Goal:** Return the maximum number of ice cream bars he can afford.

**Constraint:** The solution must be implemented using **counting sort**.

---

## Approach / Thought Process

The key insight is that to maximize the *number* of bars bought (not total value),
the greedy strategy is to always buy the **cheapest available bars first**. Buying
cheap bars first leaves more coins available for additional purchases later, which
maximizes the count.

Counting sort fits naturally here because:
- Ice cream prices are bounded (small range of values), which is exactly the kind
  of input counting sort is suited for.
- Sorting via counting sort avoids the `O(n log n)` cost of comparison-based sorts.

**Steps:**

1. **Build a frequency table (`count`)** — for each possible price from `0` up to
   `max(costs)`, count how many bars exist at that price.
   ```python
   count = [0] * (max(costs) + 1)
   for cost in costs:
       count[cost] += 1
   ```

2. **Walk through prices in increasing order** — since `count` is indexed by price,
   iterating through it from index `1` upward visits prices from cheapest to most
   expensive, which is effectively "sorted order" without ever calling `.sort()`.

3. **Greedily buy bars at each price level**:
   - Skip prices with no bars available (`count[price] == 0`).
   - Otherwise, compute how many bars at this price the boy can afford:
     `afford = coins // price`
   - He can only buy as many as actually exist at that price, so take the smaller
     of the two: `bought = min(afford, count[price])`
   - Update the running total and remaining coins:
     ```python
     n += bought
     coins -= bought * price
     ```

4. Return the running total `n` once all prices have been checked.

---

## Solution Code

```python
class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        n = 0
        count = [0] * (max(costs) + 1)
        for cost in costs:
            count[cost] += 1
        for price in range(1, len(count)):
            if count[price] == 0:
                continue
            afford = coins // price
            bought = min(afford, count[price])
            n += bought
            coins -= bought * price
        return n
```

---

## Complexity Analysis

Let `n` = number of ice cream bars, and `k` = maximum price in `costs`.

### Time Complexity: `O(n + k)`
- Building the `count` array takes `O(n)` (one pass over `costs`).
- Iterating through `count` to "buy" bars takes `O(k)`, since `count` has `k + 1`
  entries.
- Total: `O(n + k)`, which is faster than a comparison-sort-based approach
  (`O(n log n)`) when `k` is small relative to `n log n`.

### Space Complexity: `O(k)`
- The `count` array requires `k + 1` slots, where `k` is the maximum price.
- No other significant extra space is used (a few scalar variables only).

---

## Example Walkthrough

Given `costs = [1, 3, 2, 4, 1]` and `coins = 7`:

| Step | Price | Available | Affordable | Bought | Coins Left | Total Bars |
|------|-------|-----------|------------|--------|------------|------------|
| 1    | 1     | 2         | 7          | 2      | 5          | 2          |
| 2    | 2     | 1         | 2          | 1      | 3          | 3          |
| 3    | 3     | 1         | 1          | 1      | 0          | 4          |
| 4    | 4     | 1         | 0          | 0      | 0          | 4          |

**Result: 4 ice cream bars**