# Maximum Subarray (Kadane's Algorithm)

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum and return its sum.

**Examples:**
```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum 6

Input: nums = [1]
Output: 1

Input: nums = [5, 4, -1, 7, 8]
Output: 23
```

---

## Approach 1: Brute Force

Check every possible subarray and track the maximum sum.

```python
maxs = nums[0]
for i in range(len(nums)):
    current = 0
    for j in range(i, len(nums)):
        current += nums[j]
        maxs = max(maxs, current)
return maxs
```

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

---

## Approach 2: Kadane's Algorithm (Optimal)

### What is Kadane's Algorithm?

Kadane's Algorithm is a famous greedy algorithm that solves the maximum subarray problem in a single pass.

The core idea is simple — at every element, you make a greedy choice:
- If the current running sum is **negative**, drop it and start fresh from the current element
- If the current running sum is **positive**, extend the subarray by adding the current element

A negative running sum only hurts whatever comes next, so there's no point carrying it forward.

### Trace Through Example:

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=0: sums=-2,  maxs=-2
i=1: sums<0 → sums=1,   maxs=1
i=2: sums=-2,  maxs=1
i=3: sums<0 → sums=4,   maxs=4
i=4: sums=3,   maxs=4
i=5: sums=5,   maxs=5
i=6: sums=6,   maxs=6   ← maximum!
i=7: sums=1,   maxs=6
i=8: sums=5,   maxs=6

Output: 6  ✓  (subarray [4,-1,2,1])
```

### Code:

```python
class Solution():
    def maxi(self, array):
        sums = array[0]
        maxs = array[0]

        for i in range(len(array)):
            if sums < 0:
                sums = array[i]   # start fresh
            else:
                sums += array[i]  # extend subarray
            maxs = max(sums, maxs)

        return maxs


def main():
    array = list(map(int, input("enter the elements: ").split()))
    s = Solution()
    maxi = s.maxi(array)
    print("maximum subarray sum is:", maxi)

if __name__ == "__main__":
    main()
```

---

## Key Insights

- Initialize both `sums` and `maxs` to `array[0]` to handle all-negative arrays correctly
- The greedy choice — reset when negative — is what makes this O(n)
- `maxs` is updated at every step, not just when we reset

---

## Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Kadane's Algorithm | O(n) | O(1) |