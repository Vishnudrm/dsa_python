# Third Maximum Number

## Problem Statement

Given an integer array `nums`, return the third distinct maximum number in the array. If the third maximum does not exist, return the maximum number.

---

## Examples

```
Input:  nums = [3,2,1]
Output: 1

Input:  nums = [1,2]
Output: 2

Input:  nums = [2,2,3,1]
Output: 1
```

---

## Approach 1: Set + Sort (Initial Approach)

1. **Add all elements to a set** — this automatically removes duplicates.
2. **Check length** — if fewer than 3 unique elements exist, return the maximum.
3. **Sort descending** — convert set to list, sort in descending order, return element at index 2.

### Complexity
- **Time:** O(n log n) — dominated by the sort
- **Space:** O(n) — for the set and list

### Code

```python
class Solution():
    def third(self, nums):
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        if len(seen) < 3:
            return max(seen)
        else:
            third = list(seen)
            third.sort(reverse=True)
            return third[2]
```

---

## Approach 2: Three Variables (Optimized)

Instead of sorting, track the top 3 maximums in a single pass using three variables `first`, `second`, and `third`, all initialized to `-infinity`.

For each number:
1. **Skip duplicates** — if the number already equals `first`, `second`, or `third`, skip it.
2. **Skip smaller numbers** — if the number is less than `third`, skip it.
3. **Update chain** — if greater than `first`, shift everything down: `third = second`, `second = first`, `first = nums[i]`.
4. **Update second** — if greater than `second`, shift: `third = second`, `second = nums[i]`.
5. **Update third** — otherwise assign to `third`.

If `third` is still `-infinity` at the end, fewer than 3 distinct values exist — return `first`.

### Complexity
- **Time:** O(n) — single pass through the array
- **Space:** O(1) — only three variables used

### Code

```python
class Solution():
    def third(self, nums):
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        for i in range(len(nums)):
            if nums[i] < third:
                continue
            if nums[i] == first or nums[i] == second or nums[i] == third:
                continue
            elif nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second:
                third = second
                second = nums[i]
            else:
                third = nums[i]
        if third == float("-inf"):
            return first
        return third


def main():
    nums = list(map(int, input("Enter the numbers: ").split()))
    s = Solution()
    result = s.third(nums)
    print("The third maximum number is", result)

if __name__ == "__main__":
    main()
```