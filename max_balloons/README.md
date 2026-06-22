# 1189. Maximum Number of Balloons

## Problem Description

Given a string `text`, return the maximum number of instances of the word `"balloon"` that can be formed using the characters of `text`. Each character in `text` can be used at most once.

**Examples:**

```
Input: "nlaebolko"    → Output: 1
Input: "loonbalxballpoon" → Output: 2
Input: "leetcode"     → Output: 0
```

## Approach

The word `"balloon"` requires the following characters:

| Character | Count needed |
|-----------|-------------|
| b         | 1           |
| a         | 1           |
| l         | 2           |
| o         | 2           |
| n         | 1           |

The key insight is that `l` and `o` each appear **twice** in `"balloon"`, so they need special handling.

**Steps:**
1. Map each required character to an index using a dictionary.
2. Count occurrences of each required character in `text`.
3. Divide each count by how many times that character is needed per `"balloon"` (1 or 2).
4. The answer is the **minimum** of these divided values — the bottleneck character limits how many complete words we can form.

## Solution

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = []
        alph = {"a": 0, "b": 1, "l": 2, "n": 3, "o": 4}
        need_count = [1, 1, 2, 1, 2]
        count = [0] * 5

        for ch in text:
            if ch in alph:
                count[alph[ch]] += 1

        for i in range(5):
            n.append(count[i] // need_count[i])

        return min(n)


def main():
    text = str(input("Enter the text: "))
    print(text)
    s = Solution()
    balloon_count = s.maxBalloons(text)
    print("Maximum number of balloons:", balloon_count)


if __name__ == "__main__":
    main()
```

## Complexity Analysis

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | Single pass through `text` of length n |
| **Space** | O(1) | `count`, `need_count`, and `n` are all fixed-size arrays of length 5, independent of input size |

## Notes

- The `need_count` array accounts for the double occurrence of `l` and `o` in `"balloon"`.
- The minimum across all characters is the bottleneck — even if you have 100 `b`s, you can only form as many words as your scarcest character allows.
- An alternative one-liner using Python's `Counter`:

```python
from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    c = Counter(text)
    return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])
```