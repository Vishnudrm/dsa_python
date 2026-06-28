# 14. Longest Common Prefix

## Problem Statement

Given an array of strings `strs`, write a function to find the longest common prefix string amongst all strings in the array.

If there is no common prefix, return an empty string `""`.

**Examples:**

```
Input:  strs = ["flower", "flow", "flight"]
Output: "fl"

Input:  strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints:**
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters

---

## Approach — Sort + Compare Extremes

The key insight is: after sorting the list **lexicographically**, the **first** and **last** strings are the most different from each other. Any prefix shared between these two extremes is automatically shared by every string in between.

**Steps:**
1. Handle the edge case where `strs` is empty — return `""`
2. Sort `strs` lexicographically
3. Pick `first = strs[0]` (smallest) and `second = strs[-1]` (largest)
4. Compare characters one by one between `first` and `second` up to the length of the shorter string
5. Stop as soon as a mismatch is found and return the prefix built so far

**Trace Example:**

```
strs = ["flower", "flow", "flight"]

After sort → ["flight", "flow", "flower"]

first  = "flight"
second = "flower"

i=0 → f == f ✓  result = "f"
i=1 → l == l ✓  result = "fl"
i=2 → i != o ✗  break

Output → "fl"
```

**Solution:**

```python
class Solution():
    def lon(self, strs):
        result = ""

        if not strs:
            return ""
        else:
            strs.sort()
            first = strs[0]
            second = strs[-1]

            l1 = min(len(first), len(second))

            for i in range(l1):
                if first[i] == second[i]:
                    result += first[i]
                else:
                    break

        return result
```

---

## Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n log n) | Sorting the list of `n` strings dominates |
| **Space** | O(1) | No extra data structures used; sort is in-place |

where `n` = number of strings in `strs`, `m` = length of the shortest string.

> **Note:** A more optimal approach exists in **O(n·m)** time — iterate through all strings and compare each character against the first string directly, shrinking the prefix on mismatch. This avoids the O(n log n) sorting cost entirely, which is beneficial when `m << log n`.