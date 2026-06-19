# Find the Highest Altitude

This is a solution to **LeetCode 1732 — Find the Highest Altitude**.

## Problem

There is a biker going on a road trip. The road consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal to `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i` and `i + 1` for all `0 <= i < n`. A negative value means the altitude decreased.

Return the highest altitude of a point.

### Example

```
Input:  gain = [5, 9, -8, 4, 10]
Output: 20
```

Walking through it, the altitude at each point is the running total of the gains so far:

| Point | 0 | 1 | 2  | 3  | 4 | 5  |
|-------|---|---|----|----|---|----|
| Altitude | 0 | 5 | 14 | 6  | 10 | 20 |

The highest point reached is `20`.

## How the Solution Works

```python
class Solution:
    def large(self, gain: List[int]) -> int:
        large = 0
        curr = 0
        for g in gain:
            curr += g
            large = max(large, curr)
        return large
```

The key insight is that the altitude at any point is just the **cumulative sum** of all gains up to that point, starting from `0`.

- `curr` tracks the current altitude as we move through the trip, updated one gain at a time.
- `large` tracks the highest altitude seen so far.
- We start both at `0` because the trip begins at altitude `0`.
- For every gain value, we add it to `curr` (moving to the next point) and check if it's a new high with `max(large, curr)`.
- After the loop, `large` holds the highest altitude reached on the entire trip.

This avoids building a full list of altitudes — we only need to remember the running total and the maximum, not every intermediate value.

## Complexity Analysis

- **Time complexity: O(n)** — we make a single pass through the `gain` array, doing constant work per element.
- **Space complexity: O(1)** — we only use two variables (`curr` and `large`) regardless of the input size, no extra data structures.

## Running It

```
python3 alt.py
```

You'll be prompted for the number of altitude gains and then asked to enter each gain value, after which it prints the highest altitude reached.