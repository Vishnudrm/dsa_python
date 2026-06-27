# Find All Numbers Disappeared in an Array

## Problem Statement

Given an array `nums` of `n` integers where each integer is in the range `[1, n]`, return all the integers in the range that do not appear in `nums`.

**Examples:**
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]
```

---

## Approach 1: Set (Simple)

Store all numbers in a set, then check which numbers from `1` to `n` are missing.

```python
class Solution():
    def dis(self, nums):
        output = set(nums)
        out = []
        for i in range(1, len(nums) + 1):
            if i not in output:
                out.append(i)
        return out
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) — set stores all elements

---

## Approach 2: Index Marking (O(1) Space)

Since numbers are in range `[1, n]`, we can use the array indices as markers.

**Idea:**
- For each number, go to that index and mark it negative
- After marking, any index still positive means that number is missing

**Trace:**
```
nums = [4,3,2,7,8,2,3,1]

see 4 → mark index 3 → [4,3,2,-7,8,2,3,1]
see 3 → mark index 2 → [4,3,-2,-7,8,2,3,1]
see 2 → mark index 1 → [4,-3,-2,-7,8,2,3,1]
see 7 → mark index 6 → [4,-3,-2,-7,8,2,-3,1]
see 8 → mark index 7 → [4,-3,-2,-7,8,2,-3,-1]
see 2 → mark index 1 → [4,-3,-2,-7,8,2,-3,-1]
see 3 → mark index 2 → [4,-3,-2,-7,8,2,-3,-1]
see 1 → mark index 0 → [-4,-3,-2,-7,8,2,-3,-1]

index 4 (value 8 > 0) → missing number 5
index 5 (value 2 > 0) → missing number 6

Output: [5, 6] ✓
```

```python
class Solution:
    def findDisappearedNumbers(self, nums):
        out = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i + 1)
        return out
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) — modifies array in place

---

## Key Insights

- `abs(nums[i])` is needed because a number may already be marked negative from a previous step
- `i + 1` because index `i` corresponds to number `i+1`
- The set approach is simpler but uses extra space

---

## Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Set | O(n) | O(n) |
| Index Marking | O(n) | O(1) |