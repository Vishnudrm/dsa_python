# Product of Array Except Self

**Platform:** LeetCode 238  
**Difficulty:** Medium  
**Topic:** Arrays, Prefix Products

---

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

You must write an algorithm that runs in **O(n)** time and **without using division**.

**Example 1:**
```
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

**Example 2:**
```
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

---

## Approach — Left and Right Prefix Products

**Idea:** For each index `i`, the answer is:

```
output[i] = product of everything to the LEFT of i
           × product of everything to the RIGHT of i
```

We precompute two arrays:
- `left[i]` → product of all elements before index `i`
- `right[i]` → product of all elements after index `i`

Then multiply them together to get the output.

**Walkthrough for `[1, 2, 3, 4]`:**

| index | left | right | output (left × right) |
|---|---|---|---|
| 0 | 1 | 24 | 24 |
| 1 | 1 | 12 | 12 |
| 2 | 2 | 4 | 8 |
| 3 | 6 | 1 | 6 |

```python
class Solution():
    def product(self, array):
        output = [1] * len(array)
        left = [1] * len(array)
        right = [1] * len(array)

        for i in range(1, len(array)):
            left[i] = left[i-1] * array[i-1]

        for i in range(len(array)-2, -1, -1):
            right[i] = right[i+1] * array[i+1]

        for i in range(len(array)):
            output[i] = left[i] * right[i]

        return output

def main():
    array = list(map(int, input("Enter the elements: ").split()))
    s = Solution()
    product = s.product(array)
    print("The product is:", product)

if __name__ == "__main__":
    main()
```

**How it works:**
- Loop 1 builds `left` going left to right — each element is the previous left product times the previous number
- Loop 2 builds `right` going right to left — each element is the next right product times the next number
- Loop 3 multiplies `left[i] * right[i]` to get the final answer at each index

---

## Complexity

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | Three separate single passes through the array |
| **Space** | O(n) | Two extra arrays of size n for left and right products |

---

## Key Takeaway

The trick is recognising that `output[i] = left_product × right_product`. This avoids division entirely and keeps the solution linear by precomputing prefix products from both directions.