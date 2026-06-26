# Rotate Image

## Problem Statement

Given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees clockwise **in-place**.

You must modify the input matrix directly without allocating another 2D matrix.

**Example:**
```
Input:
1 2 3
4 5 6
7 8 9

Output:
7 4 1
8 5 2
9 6 3
```

---

## Approach 1: Brute Force (Extra Space)

Create a new matrix and place each element at its rotated position using the formula:

`(i, j)` → `(j, n-1-i)`

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n²) — extra matrix needed

This violates the in-place constraint, so we need a better approach.

---

## Approach 2: Transpose + Reverse Rows (Optimal)

The key insight is that a 90 degree clockwise rotation can be broken into two simple steps:

**Step 1: Transpose the matrix**
Swap every element `(i, j)` with `(j, i)` — converting rows into columns.

```
1 2 3        1 4 7
4 5 6   →    2 5 8
7 8 9        3 6 9
```

**Step 2: Reverse each row**

```
1 4 7        7 4 1
2 5 8   →    8 5 2
3 6 9        9 6 3
```

This gives us the 90 degree clockwise rotation!

```python
class Solution():
    def img(self, matrix):
        # Step 1: Transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
        
        return matrix


def main():
    n = int(input("enter the size of the matrix: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"enter row {i}: ").split()))
        matrix.append(row)
    s = Solution()
    img = s.img(matrix)
    print("the rotated image is:", img)

if __name__ == "__main__":
    main()
```

---

## Key Insights

- **Transpose loop bounds:** `j` starts from `i+1` to avoid double-swapping which would undo the transpose
- `row.reverse()` needs parentheses — `row.reverse` without `()` does nothing
- Columns can't be directly reversed in Python like rows, which is why transpose + row reverse is the elegant solution

---

## Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(n²) |
| Transpose + Reverse | O(n²) | O(1) |