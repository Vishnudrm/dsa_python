# Intersection of Two Arrays

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

---

## Examples

```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

---

## Approach

1. **Convert `nums1` to a set** — This gives O(1) lookup time for checking if an element exists.

2. **Iterate through `nums2`** — For each element, check if it exists in the set.

3. **Add to result set** — Using a set for result automatically handles duplicates.

4. **Return as list** — Convert the result set to a list before returning.

---

## Complexity

- **Time:** O(n + m) — one pass to build the set, one pass through nums2
- **Space:** O(n) — for the seen set storing elements of nums1

---

## Code

```python
class Solution():
    def inter(self, nums1, nums2):
        result = set()
        seen = set(nums1)
        for i in range(len(nums2)):
            if nums2[i] in seen:
                result.add(nums2[i])
        return list(result)


def main():
    nums1 = list(map(int, input("Enter the first list: ").split()))
    nums2 = list(map(int, input("Enter the second list: ").split()))
    s = Solution()
    intersection = s.inter(nums1, nums2)
    print("Intersection of 2 arrays:", intersection)

if __name__ == "__main__":
    main()
```