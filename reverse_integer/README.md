# Reverse Integer (LeetCode #7)

## Problem

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return `0`.

**Constraint:** Assume the environment does not allow storing 64-bit integers (signed or unsigned).

### Examples

| Input | Output |
|-------|--------|
| `123` | `321` |
| `-123` | `-321` |
| `120` | `21` |

## Approach

1. Record the sign of `x`, then work with its absolute value.
2. Repeatedly extract the last digit using `x % 10` and shrink `x` using integer division `x //= 10`.
3. Build the reversed number digit by digit: `result = result * 10 + digit`.
4. Before each update, check whether adding the next digit would push `result` past `INT_MAX` (`2^31 - 1`). If so, return `0` immediately instead of letting the value overflow.
5. Re-apply the sign at the end and return the result.

This pre-check (rather than reversing first and validating the range afterward) is what lets the solution work without ever needing a type wider than 32 bits.

## Solution (Python)

```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Overflow check happens before the multiply/add
            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result
```

## Complexity

**Time Complexity: O(log₁₀ x)**
Each iteration removes one digit from `x` via integer division, so the loop runs once per digit in the input — proportional to the number of digits, i.e. `log₁₀(x)`.

**Space Complexity: O(1)**
Only a fixed number of scalar variables (`sign`, `result`, `digit`) are used regardless of input size; no auxiliary data structures grow with the input.

## Edge Cases Handled

- Negative numbers (sign preserved correctly).
- Trailing zeros in the input that become leading zeros when reversed (e.g. `120 → 21`).
- Reversed values that would overflow 32-bit signed integer bounds (e.g. `1534236469 → 0`).