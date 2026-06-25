# 495. Teemo Attacking

## Problem

Teemo attacks an enemy at timestamps given in `timeSeries`. Each attack poisons the enemy for `duration` seconds. If a new attack happens before the poison expires, the timer resets. Find the total seconds the enemy is poisoned.

**Example 1:**
```
Input:  timeSeries = [1, 4], duration = 2
Output: 4
```

**Example 2:**
```
Input:  timeSeries = [1, 2], duration = 2
Output: 3
```

---

## Approach — Greedy Overlap Tracking

Track until when the poison is active (`poison`) and accumulate only the effective poisoned time.

**Two cases for each attack:**
1. **No overlap** — new attack starts after poison expires → add full `duration`
2. **Overlap** — new attack cuts previous poison short → add only the remaining effective time

**Trace for `[1, 4], duration = 2`:**
```
i=0: array[0]=1, poison=0 → no overlap → poison=3, time=2
i=1: array[1]=4, poison=3 → no overlap → poison=6, time=4
return 4 ✅
```

**Trace for `[1, 2], duration = 2`:**
```
i=0: array[0]=1, poison=0 → no overlap → poison=3, time=2
i=1: array[1]=2, poison=3 → overlap! curr=2-(3-2)=1 → poison=4, time=3
return 3 ✅
```

---

## Complexity

| | |
|---|---|
| Time | O(n) — single pass through timeSeries |
| Space | O(1) — no extra data structures |

---

## Key Insights

- `poison` tracks the timestamp until which poison is currently active
- `curr` computes effective duration when a new attack overlaps: `duration - (poison - array[i])`
- When `poison <= array[i]`, the previous poison has already expired → add full duration
- When `poison > array[i]`, the new attack cuts short the previous one → add only the gap

---

## Files
- `teemo.py` — runnable solution with CLI input