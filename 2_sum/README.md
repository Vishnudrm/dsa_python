# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

- Exactly one valid answer is assumed to exist (per LeetCode's constraints).
- You may not use the same element twice.
- Return the answer in any order.

**Example:**
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

## Approach: One-Pass Hash Map

Use a dictionary to store each number we've already seen, mapped to its index. For each new number, check whether its **complement** (`target - num`) already exists in the dictionary. If it does, we've found our pair.

```python
class Solution:
    def sums(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i
        return []
```

### Why check before inserting?

The complement check happens **before** `nums[i]` is added to `seen`. This guarantees:
- We never match an element with itself (e.g. `nums=[3]`, `target=6` won't falsely return `[0, 0]`).
- `seen` only ever contains indices that come *before* the current one, so the first index in the returned pair is always the earlier one.

### Trace

`nums = [1, 1, 2, 3, 4]`, `target = 7`

| i | nums[i] | complement | complement in seen? | seen (after) |
|---|---------|------------|----------------------|---------------|
| 0 | 1       | 6          | no                   | {1: 0}        |
| 1 | 1       | 6          | no                   | {1: 1}        |
| 2 | 2       | 5          | no                   | {1: 1, 2: 2}  |
| 3 | 3       | 4          | no                   | {1: 1, 2: 2, 3: 3} |
| 4 | 4       | 3          | **yes** → return [3, 4] |            |

Note: `seen[1]` gets overwritten from `0` to `1` when the second `1` is processed. This is fine — we only care about the *most recent* prior index for any duplicate value, since it's always a valid earlier match.

## Complexity Analysis

| | Complexity |
|---|---|
| Time | O(n) — single pass, O(1) average dict lookups |
| Space | O(n) — dictionary can hold up to n entries |

## Common Bugs

- **Two-pass instead of one-pass:** Building the full dictionary first, then looping again to check complements, works but does 2x the work. It also requires an extra `dictionary[j] != i` check to avoid matching an element with itself — the one-pass version avoids this entirely by checking *before* inserting.
- **No `return` after the loop:** If no pair sums to target, the function falls off the end and implicitly returns `None`. Decide explicitly whether you want `None`, `[]`, or something else — don't let it happen by accident.
- **Naming clash with built-ins:** Avoid naming a method `sum` — it shadows Python's built-in `sum()` function within that scope.
- **Off-by-one / wrong index returned:** Since `seen[complement]` is looked up *before* the current index `i` is added, make sure the returned pair is `[seen[complement], i]` and not `[i, seen[complement]]` if order matters (though LeetCode accepts any order).