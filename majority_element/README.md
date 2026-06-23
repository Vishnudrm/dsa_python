# Majority Element

**Platform:** LeetCode 169  
**Difficulty:** Easy  
**Topic:** Arrays, HashMap, Boyer-Moore Voting Algorithm

---

## Problem Description

Given an array `nums` of size `n`, return the **majority element** — the element that appears more than `n/2` times.

You may assume the majority element always exists in the array.

**Example:**
```
Input:  nums = [2, 2, 1, 1, 2]
Output: 2

Input:  nums = [10, 9, 9, 9, 10]
Output: 9
```

---

## Approach 1 — HashMap (Dictionary)

**Idea:** Count the frequency of every element using a dictionary, then return the key with the highest count.

```python
class Solution:
    def majorityElement(self, elements):
        count = {}
        for i in range(len(elements)):
            if elements[i] in count:
                count[elements[i]] += 1
            else:
                count[elements[i]] = 1
        return max(count, key=count.get)

def main():
    elements = list(map(int, input("Enter the elements in the list: ").split()))
    s = Solution()
    major = s.majorityElement(elements)
    print("The majority element is", major)

if __name__ == "__main__":
    main()
```

**How it works:**
- Build a frequency map of all elements
- `max(count, key=count.get)` returns the key whose value (frequency) is the largest
- Since the majority element appears more than n/2 times, it will always have the highest count

### Complexity

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | One pass to build the dictionary, one pass for max |
| **Space** | O(n) | Dictionary stores up to n distinct elements |

---

## Approach 2 — Boyer-Moore Voting Algorithm

**Idea:** The majority element appears more than n/2 times. If you cancel every occurrence of the majority element with a different element, the majority element always survives.

For example, in `[2, 2, 1, 1, 2]` — cancel every `2` with a `1`, and `2` is still left standing.

```python
class Solution():
    def majority(self, elements):
        candidate = elements[0]
        count = 1
        for i in range(1, len(elements)):
            if count == 0:
                candidate = elements[i]
                count = 1
            elif elements[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate

def main():
    elements = list(map(int, input("Enter the elements in the list: ").split()))
    s = Solution()
    major = s.majority(elements)
    print("The majority element is", major)

if __name__ == "__main__":
    main()
```

**How it works:**
- Start with `candidate = elements[0]` and `count = 1`
- For each element:
  - If `count == 0` → pick current element as new candidate, reset count to 1
  - If current element matches candidate → `count += 1`
  - Else → `count -= 1` (cancel out)
- The candidate that survives is the majority element

**Key insight:** Since the majority element appears more than n/2 times, it can never be fully cancelled out by the minority elements combined.

### Complexity

| | Complexity | Reason |
|---|---|---|
| **Time** | O(n) | Single pass through the array |
| **Space** | O(1) | Only two variables used — `candidate` and `count` |

---

## Comparison

| | Time | Space | Notes |
|---|---|---|---|
| HashMap | O(n) | O(n) | Intuitive, easy to implement |
| Boyer-Moore | O(n) | O(1) | Optimal — no extra space needed |

Boyer-Moore is the preferred solution in interviews as it achieves optimal time and space simultaneously.