# 350. Intersection of Two Arrays II

## Problem

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it appears in both arrays.

**Example 1:**
```
Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

**Example 2:**
```
Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

---

## Approach — Remove on Match

Loop through `nums2`. For each element, check if it exists in `nums1`. If it does, add it to the result and remove it from `nums1` so the same element can't be matched again.

**Trace for `nums1 = [1,2,2,1], nums2 = [2,2]`:**
```
i=0: nums2[0]=2 → in nums1? ✅ → result=[2], nums1=[1,2,1]
i=1: nums2[1]=2 → in nums1? ✅ → result=[2,2], nums1=[1,1]
return [2,2] ✅
```

---

## Complexity

| | |
|---|---|
| Time | O(n×m) — for each element in nums2, `in` and `remove` scan nums1 |
| Space | O(min(n,m)) — result array |

---

## Key Insights

- `nums1.remove(x)` removes only the **first occurrence** of `x` — this handles duplicates correctly
- Removing matched elements from `nums1` prevents the same element from being matched twice
- Order of result depends on the order of `nums2`

---

## Alternative Approach — HashMap (O(n+m) time)

```python
from collections import Counter
def intersect(nums1, nums2):
    count = Counter(nums1)
    result = []
    for num in nums2:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1
    return result
```

---

## Files
- `intersect.py` — runnable solution with CLI input