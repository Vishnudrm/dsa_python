# Contains Duplicate

**File:** `duplicates.py`

## Problem Statement
Given an integer array `nums`, determine whether any value appears **at least twice** in the array.

- Return `True` if any value appears more than once.
- Return `False` if every element is distinct.

**Example 1:**
```
Input:  nums = [1, 2, 3, 1]
Output: True
Explanation: 1 appears at index 0 and index 3.
```

**Example 2:**
```
Input:  nums = [1, 2, 3, 4]
Output: False
Explanation: All elements are distinct.
```

**Example 3:**
```
Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
```

**Constraints:**
- `0 <= nums.length`
- Array elements are integers (can be negative, zero, or positive).

## Approach
The brute-force way to solve this is comparing every pair of elements (nested loop), which costs O(n²) time. A better approach is to sort the array first and check adjacent elements for equality, which costs O(n log n) time. The optimal approach, used here, trades a bit of space for linear time:

1. Create an empty hash set `seen` to keep track of numbers encountered so far.
2. Iterate through `nums` from left to right, one element at a time.
3. For the current number:
   - If it is **already present** in `seen`, that means it occurred earlier in the array → a duplicate is found, so return `True` immediately (no need to scan further).
   - If it is **not present**, add it to `seen` and move on to the next element.
4. If the loop finishes without ever finding a repeated number, return `False` — every element was distinct.

This works because a hash set gives average O(1) time for both membership checks (`in`) and insertions (`add`), so the whole array can be checked in a single pass.

### Edge Cases Considered
- **Empty array (`[]`):** `range(len(nums))` is empty, so the loop body never executes → returns `False` directly.
- **Single element (`[5]`):** Only one iteration happens, `seen` is empty at that point, so no duplicate can exist → returns `False`.
- **All identical elements (`[1, 1, 1]`):** Duplicate is caught as early as the second element → returns `True` immediately, without scanning the rest.

## Solution
```python
class Solution():
	def duplicates(self,nums):
		seen=set()
		for i in range(len(nums)):
			if nums[i] in seen:
				return True
			else:
				seen.add(nums[i])
		return False
			
def main():
	nums=list(map(int,input("enter the numbers in the array:").split()))
	s=Solution()
	dupli=s.duplicates(nums)
	print(dupli)
	
if __name__=="__main__":
	main()
```

## Complexity Analysis
- **Time Complexity:** O(n)
  The array is traversed exactly once. Each `in` check and `add` operation on the set runs in average O(1) time, so the total work is proportional to the number of elements, `n`.

- **Space Complexity:** O(n)
  In the worst case (no duplicates at all), every element of `nums` ends up stored in the `seen` set, requiring extra space proportional to `n`.

## Usage
```bash
python duplicates.py
enter the numbers in the array: 1 2 3 4 1
```
Output:
```
True
```