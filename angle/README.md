# Angle Between Hands of a Clock

## Problem Description

Given the current time as an `hour` (1 to 12) and `minutes` (0 to 59), find the
smaller angle (in degrees) formed between the hour hand and the minute hand of an
analog clock.

**Key detail:** The hour hand does not jump instantly from one number to the next
— it moves continuously and gradually as the minutes pass within that hour. For
example, at `3:30`, the hour hand isn't sitting exactly on the "3"; it has drifted
halfway toward the "4".

---

## Approach / Thought Process

A standard analog clock face is a full circle of `360°`, divided across `12` hour
marks and `60` minute marks.

**Step 1: Minute hand angle**
The minute hand sweeps the full `360°` circle in `60` minutes, so it moves:
```
360 / 60 = 6° per minute
```
So its angle from the 12 o'clock position is simply:
```python
min_angle = minutes * 6
```

**Step 2: Hour hand angle**
The hour hand sweeps the full `360°` circle in `12` hours, so it moves:
```
360 / 12 = 30° per hour
```
But it also drifts continuously *within* each hour, based on how many minutes have
passed. Over a full 60-minute hour, the hour hand also moves `30°` (the gap to the
next hour mark), so its drift rate is:
```
30 / 60 = 0.5° per minute
```
Combining the base hour position with the within-hour drift:
```python
hour_angle = hour * 30 + minutes * 0.5
```

**Step 3: Raw angle between the hands**
```python
angle = abs(hour_angle - min_angle)
```

**Step 4: Handle the circular wraparound**
The raw difference can be more than `180°`, but on a circle, two hands are always
considered to form the *smaller* of the two possible angles between them (going
clockwise or counterclockwise). So the final answer is:
```python
return min(angle, 360 - angle)
```

**Edge case note:** When `hour == 12`, `hour * 30` evaluates to `360°` instead of
`0°`. This might look like a bug, but it isn't — the final `min(angle, 360 - angle)`
step automatically corrects for any full-rotation offset, since adding `360°`
anywhere in the calculation doesn't change which of the two complementary angles is
smaller.

---

## Solution Code

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes * 6
        hour_angle = hour * 30 + 0.5 * minutes
        angle = abs(hour_angle - min_angle)
        return min(angle, 360 - angle)
```

---

## Complexity Analysis

### Time Complexity: `O(1)`
The solution only performs a fixed number of arithmetic operations regardless of
input size — there are no loops or recursive calls.

### Space Complexity: `O(1)`
Only a constant number of scalar variables (`min_angle`, `hour_angle`, `angle`) are
used, independent of input values.

---

## Example Walkthrough

Given `hour = 3, minutes = 30`:

| Step | Calculation                  | Result |
|------|-------------------------------|--------|
| Minute angle | `30 * 6`               | `180°` |
| Hour angle   | `3 * 30 + 0.5 * 30`     | `105°` |
| Raw difference | `abs(105 - 180)`      | `75°`  |
| Final angle  | `min(75, 360 - 75)`     | `75°`  |

**Result: 75.0°**

Given `hour = 12, minutes = 0` (edge case):

| Step | Calculation                  | Result |
|------|-------------------------------|--------|
| Minute angle | `0 * 6`                 | `0°`   |
| Hour angle   | `12 * 30 + 0.5 * 0`     | `360°` |
| Raw difference | `abs(360 - 0)`         | `360°` |
| Final angle  | `min(360, 360 - 360)`   | `0°`   |

**Result: 0.0°** — correctly shows both hands overlapping at 12:00.