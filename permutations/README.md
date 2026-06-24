# Permutations

## Problem Statement

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

---

## Examples

```
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input:  nums = [0,1]
Output: [[0,1],[1,0]]

Input:  nums = [1]
Output: [[1]]
```

---

## Approach: Insertion-Based Recursion

The idea is to build permutations by inserting the first element into every possible position of all permutations of the remaining elements.

1. **Base case** — if the array is empty, return `[[]]` (one empty permutation).
2. **Recurse** — get all permutations of `array[1:]`.
3. **Insert** — for each permutation `p`, insert `array[0]` at every possible position (0 to `len(p)`).
4. **Collect** — add each resulting permutation to the result.

**Example for `[1, 2, 3]`:**
- `permu([2, 3])` → `[[2, 3], [3, 2]]`
- Insert `1` into `[2, 3]` → `[1,2,3]`, `[2,1,3]`, `[2,3,1]`
- Insert `1` into `[3, 2]` → `[1,3,2]`, `[3,1,2]`, `[3,2,1]`

---

## Complexity

- **Time:** O(n × n!) — there are n! permutations and each takes O(n) to build
- **Space:** O(n!) — to store all permutations

---

## Code

```python
class Solution:
    def permu(self, array):
        result = []
        if len(array) == 0:
            return [[]]
        else:
            perms = self.permu(array[1:])
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, array[0])
                    result.append(p_copy)
        return result


def main():
    array = list(map(int, input("Enter the elements: ").split()))
    s = Solution()
    perm = s.permu(array)
    print("The permutations are", perm)

if __name__ == "__main__":
    main()
```