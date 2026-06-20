# Valid Parentheses

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples

| Input        | Output  |
|--------------|---------|
| `"()"`       | `true`  |
| `"()[]{}"`   | `true`  |
| `"(]"`       | `false` |
| `"([])"`     | `true`  |
| `"([)]"`     | `false` |

---

## Approach

This is solved using a **stack**, since brackets must close in the exact reverse order they were opened — a classic Last-In-First-Out (LIFO) pattern.

A dictionary `pairs` maps each opening bracket to its matching closing bracket:

```python
pairs = {'(': ')', '{': '}', '[': ']'}
```

Walking through the string character by character:

1. **If the character is an opening bracket** (i.e. a key in `pairs`) → push it onto the stack.
2. **If the character is a closing bracket:**
   - If the stack is empty, there's nothing for it to match → invalid.
   - Otherwise, pop the top of the stack (`j`) and check whether `pairs[j]` equals the current character.
     - If they don't match, the brackets are mismatched or out of order → invalid.
     - If they match, continue.
3. **At the end**, the string is valid only if the stack is empty — every opener must have been matched and popped. A non-empty stack means there are unclosed brackets left over.

### Why a stack works

The most recently opened bracket must be the next one closed. A stack naturally enforces this: pushing on open, popping on close, and comparing against the top ensures both correct **type** and correct **order** are checked in one pass.

### Trace example — `"([)]"` (invalid)

| Step | Char | Action                              | Stack       |
|------|------|--------------------------------------|-------------|
| 1    | `(`  | push                                  | `['(']`     |
| 2    | `[`  | push                                  | `['(', '[']`|
| 3    | `)`  | pop `'['`, expects `']'`, got `')'`  | mismatch → `False` |

---

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    j = stack.pop()
                    if pairs[j] != char:
                        return False

        return len(stack) == 0
```

---

## Complexity

### Time Complexity: `O(n)`
Each character in the string is processed exactly once — one push or one pop — so the work scales linearly with the length of the string `n`.

### Space Complexity: `O(n)`
In the worst case (e.g. a string of all opening brackets like `"((((("`), every character gets pushed onto the stack, so the stack can grow up to size `n`.

---

## Edge Cases Handled

- **Empty string** → valid (`stack` stays empty, loop never runs).
- **Lone closing bracket** (e.g. `")"`) → stack is empty when encountered → invalid.
- **Lone opening bracket** (e.g. `"("`) → stack non-empty at the end → invalid.
- **Wrong order** (e.g. `"([)]"`) → caught by the mismatch check before reaching the end.