# Add Binary

## Problem Description

Given two binary strings `a` and `b`, return their sum as a binary string.

### Examples

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

### Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

---

## Solution Approach

The idea is to simulate **manual binary addition**, just like adding two numbers by hand — column by column, from right to left, while keeping track of a carry.

### Steps

1. Use two pointers, `i` and `j`, starting at the **last index** of `a` and `b` respectively (since addition starts from the least significant bit).
2. Maintain a `carry` variable, initialized to `0`.
3. Loop while there are still digits left in `a`, digits left in `b`, **or** a carry remaining:
   - Get the current digit of `a` (`v1`) — use `0` if `i` has gone out of bounds.
   - Get the current digit of `b` (`v2`) — use `0` if `j` has gone out of bounds.
   - Compute `total = v1 + v2 + carry`.
   - The digit for this column is `total % 2`.
   - The new carry is `total // 2`.
   - Append the digit to a result list.
   - Move both pointers one step to the left (`i -= 1`, `j -= 1`).
4. Since digits were collected from least significant to most significant, **reverse** the result list and join it into a string.

### Why this works

At any column, the sum of two binary digits plus a carry can only be **0, 1, 2, or 3**:

| total | digit (`total % 2`) | carry (`total // 2`) |
|-------|----------------------|------------------------|
| 0     | 0                    | 0                      |
| 1     | 1                    | 0                      |
| 2     | 0                    | 1                      |
| 3     | 1                    | 1                      |

This mirrors exactly how binary addition works: `1 + 1 = 10` (write `0`, carry `1`), and `1 + 1 + 1 = 11` (write `1`, carry `1`).

### Code

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0

            total = v1 + v2 + carry
            carry = total // 2
            result.append(str(total % 2))

            i -= 1
            j -= 1

        return ''.join(reversed(result))
```

---

## Complexity Analysis

### Time Complexity: `O(max(n, m))`

Where `n = len(a)` and `m = len(b)`. The loop runs once for each digit in the longer string (plus possibly one extra iteration if there's a final carry), and each iteration does constant-time work.

### Space Complexity: `O(max(n, m))`

The `result` list stores one character per digit of the output, and the output has at most `max(n, m) + 1` digits (the `+1` accounts for a possible carry-out at the most significant bit). The final `''.join(...)` also creates a new string of this size.