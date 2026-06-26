# Distribute Candies

## Problem Statement

Alice has `n` candies, where `n` is always even. Each candy has a type represented by an integer. Alice wants to eat `n/2` candies but also wants to eat as many **unique types** as possible.

Return the maximum number of different types of candies Alice can eat.

**Examples:**
```
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can eat one of each type [1,2,3]

Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can only eat 2 candies. Best to pick types 2 and 3.

Input: candyType = [6,6,6,6]
Output: 1
Explanation: Only one unique type exists.
```

---

## Approach: Set + Min (Optimal)

The key insight is:
- Alice can eat `n // 2` candies total
- She wants maximum unique types
- Unique types = `len(set(candyType))`
- Answer = `min(unique types, n // 2)`

If there are more unique types than she can eat, she's limited by `n // 2`.
If there are fewer unique types than she can eat, she's limited by the number of unique types.

```python
class Solution():
    def maximum(self, candies):
        sets = set(candies)
        return min(len(sets), len(candies) // 2)


def main():
    candies = list(map(int, input("enter the types of candies: ").split()))
    s = Solution()
    result = s.maximum(candies)
    print("maximum number of candies:", result)

if __name__ == "__main__":
    main()
```

---

## Key Insights

- `set()` automatically removes duplicates, giving unique candy types
- Use `//` for integer division instead of `/` to avoid floats
- One line solution once you see the pattern!

---

## Complexity Analysis

| | Complexity |
|---|---|
| Time | O(n) — building the set |
| Space | O(n) — set stores unique elements |