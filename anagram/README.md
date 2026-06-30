# Valid Anagram

## Problem
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram is formed by rearranging the letters of a word using all the original letters exactly once.

**Example:**
```
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False
```

## Approach: Single Hash Map (Increment/Decrement)

Instead of building two separate frequency dictionaries and comparing them, this solution uses **one** dictionary:

1. If `len(s) != len(t)`, they can't be anagrams — return `False` immediately.
2. Loop through `s`, incrementing the count for each character in `sd`.
3. Loop through `t`, decrementing the count for each character in `sd`.
   - If a character in `t` isn't a key in `sd` at all, `s` never had it — return `False` right away.
4. After both loops, every count in `sd` should be exactly `0` if the strings are true anagrams. Loop through `sd`'s values — if any is nonzero, return `False`.
5. If nothing failed, return `True`.

### Why this works
Each character increments once per occurrence in `s` and decrements once per occurrence in `t`. If both strings contain the exact same characters with the exact same frequencies, every count cancels out to zero.

## Complexity
- **Time:** O(n + m) — one pass through `s`, one pass through `t`, one pass through the dictionary (bounded by alphabet size). Since `n == m` is required to proceed, this simplifies to O(n).
- **Space:** O(k), where `k` is the number of distinct characters (at most 26 for lowercase English letters, or O(n) in the general/unicode case).

This is optimal — every character must be examined at least once, so O(n) is the best possible time complexity for this problem.

## Other Approaches Considered
| Approach | Time | Space | Notes |
|---|---|---|---|
| Sort both strings, compare | O(n log n) | O(n) | Simple but not optimal |
| Two separate count dictionaries | O(n + m) | O(n + m) | Correct, but uses 2x the space of the single-map version |
| Single count dictionary (this solution) | O(n) | O(k) | Most space-efficient, same optimal time |

## How to Run
```bash
python3 valid_anagram.py
```
You'll be prompted to enter two strings, and it will print `True` or `False`.

## Common Bugs Hit While Solving This
- Reassigning `s`/`t` to empty lists before using them (losing the original input).
- Mismatching dictionary keys vs. loop indices (`sd[i] += 1` instead of `sd[s[i]] += 1`).
- An `else: return True` inside the final verification loop, which exits after checking only the *first* key instead of all of them.
- Overwriting the input variable `s` with the `Solution()` instance in `main()`, then accidentally passing the object instead of the string.