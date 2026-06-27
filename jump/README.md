# Jump Game II

## Problem Statement

Given a 0-indexed array `nums`, where `nums[i]` represents the maximum jump length from index `i`, return the **minimum number of jumps** to reach the last index. You start at index 0.

**Examples:**
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: Jump from index 0 to 1 (value 3), then to last index.

Input: nums = [2,3,0,1,4]
Output: 2
```

---

## Approach 1: Brute Force (BFS)

Try all possible jumps at each step and find the minimum using BFS level by level.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

## Approach 2: Greedy (Optimal)

### Idea

Think of jumps as **levels**. From your current level, find the farthest you can reach. When you exhaust the current level, take a jump and move to the next level.

Three variables:
- `farthest` — farthest index reachable so far
- `end` — end of current jump level
- `jumps` — number of jumps taken

When `i == end`, you've exhausted the current level → take a jump, extend `end` to `farthest`.

### Trace:
```
nums = [2, 3, 1, 1, 4]
jumps=0, farthest=0, end=0

i=0: farthest=max(0, 0+2)=2,  i==end → jumps=1, end=2
i=1: farthest=max(2, 1+3)=4,  i!=end
i=2: farthest=max(4, 2+1)=4,  i==end → jumps=2, end=4
i=3: farthest=max(4, 3+1)=4,  i!=end

return 2 ✓
```

### Code:
```python
class Solution():
    def jumps(self, nums):
        farthest = 0
        end = 0
        jump = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jump += 1
                end = farthest
        return jump


def main():
    nums = list(map(int, input("enter the elements: ").split()))
    s = Solution()
    jump = s.jumps(nums)
    print("the number of jumps is:", jump)

if __name__ == "__main__":
    main()
```

---

## Key Insights

- Loop runs until `len(nums) - 1` — no need to jump from the last index
- `farthest = max(farthest, i + nums[i])` — always track the best reachable index
- `end = farthest` when jumping — extend to the best reachable from current level
- Greedy works here because taking the farthest jump at each level is always optimal

---

## Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n²) | O(n) |
| Greedy | O(n) | O(1) |