# Contains Duplicate II

## Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if there exist two distinct indices `i` and `j` such that:
- `nums[i] == nums[j]`
- `abs(i - j) <= k`

Otherwise return `False`.

**Examples:**
```
Input: nums = [1, 2, 3, 1], k = 3   → Output: True
Input: nums = [1, 2, 3, 1, 2, 3], k = 2  → Output: False
Input: nums = [1, 0, 1, 1], k = 1   → Output: True
```

---

## Approach 1: Brute Force

Check every pair of indices `(i, j)` and verify if the values are equal and the distance is within `k`.

```python
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and abs(i - j) <= k:
            return True
return False
```

- **Time Complexity:** O(n²) — nested loops over all pairs
- **Space Complexity:** O(1) — no extra space used

---

## Approach 2: HashMap (Optimal)

Use a dictionary to store each element's most recently seen index.
As we iterate, for each element we check:
1. If it exists in the dictionary and the distance to its last seen index is `<= k` → return `True`
2. If it exists but distance is `> k` → update the index to the current one (a closer match may appear later)
3. If it doesn't exist → add it to the dictionary

```python
class Solution():
    def duplicates(self, k, array):
        dictionary = {}
        for i in range(len(array)):
            if array[i] not in dictionary:
                dictionary[array[i]] = i
            elif abs(dictionary[array[i]] - i) <= k:
                return True
            else:
                dictionary[array[i]] = i
        return False
```

- **Time Complexity:** O(n) — single pass through the array
- **Space Complexity:** O(n) — dictionary stores at most n elements

---

## Key Insight

The `else` branch (updating the index) is critical — when a duplicate is found but the distance exceeds `k`, we update to the latest index. This ensures we always compare against the **closest previous occurrence**, maximizing the chance of satisfying `abs(i - j) <= k` for future duplicates.