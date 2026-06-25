# 268. Missing Number

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the one number that is missing.

**Example 1:**
```
Input:  [3, 0, 1]
Output: 2
```

**Example 2:**
```
Input:  [0, 1, 2]
Output: 3
```

**Example 3:**
```
Input:  [0, 1, 3]
Output: 2
```

---

## Approach — Presence Array (Seen Array)

Since the input contains numbers from `0` to `n`, we can create a boolean presence array of size `n+1` and mark each number we see. The index that remains unmarked is the missing number.

**Steps:**
1. Create `seen = [0] * (n + 1)` — all zeros initially
2. For each number in the array, mark `seen[number] = 1`
3. Loop through `seen` — whichever index still has `0` is the missing number

**Trace for `[3, 0, 1]`:**
```
seen = [0, 0, 0, 0]
seen[3] = 1 → [0, 0, 0, 1]
seen[0] = 1 → [1, 0, 0, 1]
seen[1] = 1 → [1, 1, 0, 1]
              index 2 is 0 → return 2 ✅
```

---

## Complexity

| | |
|---|---|
| Time | O(n) — two linear passes |
| Space | O(n) — seen array of size n+1 |

---

## Key Insights

- `seen` must be size `n+1` (not `n`) because the missing number could be `n` itself
- Store `1` (not the index `i`) to avoid ambiguity with the default value `0`
- Do NOT use `list.insert()` — it shifts elements and grows the list instead of marking in place

---

## Alternative Approaches

**Math (O(1) space):**
```python
return (len(nums) * (len(nums) + 1) // 2) - sum(nums)
```
Expected sum minus actual sum = missing number.

**XOR (O(1) space):**
```python
result = len(nums)
for i, num in enumerate(nums):
    result ^= i ^ num
return result
```
XOR of index and value cancels out all present numbers, leaving the missing one.

---

## Files
- `missing.py` — runnable solution with CLI input