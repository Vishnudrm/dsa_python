# Next Permutation

## Problem Statement

A permutation of an array of integers is an arrangement of its members into a sequence or linear order. The next permutation of an array is the next lexicographically greater permutation. If no such arrangement is possible, the array must be rearranged into the lowest possible order (ascending).

The replacement must be in place and use only constant extra memory.

---

## Examples

```
Input:  nums = [1,2,3]
Output: [1,3,2]

Input:  nums = [3,2,1]
Output: [1,2,3]

Input:  nums = [1,1,5]
Output: [1,5,1]
```

---

## Approach

The algorithm works in 4 steps:

1. **Find the pivot** — Scan from right to left and find the first index `i` where `nums[i] < nums[i+1]`. This is the pivot.

2. **Edge case** — If no pivot is found, the array is fully descending (e.g. `[3,2,1]`). Just reverse the whole array and return.

3. **Find the candidate** — Scan from right to left and find the first element greater than `nums[pivot]`. Swap it with the pivot.

4. **Reverse the suffix** — Reverse the subarray after the pivot index to get the smallest possible order for that suffix.

---

## Complexity

- **Time:** O(n) — at most three linear passes
- **Space:** O(1) — in place, no extra memory used

---

## Code

```python
class Solution():
    def next(self, nums):
        pivot = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return nums

        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        left = pivot + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


def main():
    array = list(map(int, input("Enter the elements in the array: ").split()))
    s = Solution()
    result = s.next(array)
    print("The next permuted array is", result)

if __name__ == "__main__":
    main()
```