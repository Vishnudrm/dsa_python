# Relative Ranks

## Problem Statement

Given an integer array `score` of size `n`, where `score[i]` is the score of the `ith` athlete, return an array `answer` where `answer[i]` is the rank of the `ith` athlete.

- 1st place → "Gold Medal"
- 2nd place → "Silver Medal"
- 3rd place → "Bronze Medal"
- 4th place onwards → their placement number as a string

---

## Examples

```
Input:  score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Input:  score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
```

---

## Approach

1. **Build a dictionary** — Map each score value to its original index so we can place ranks back correctly after sorting.

2. **Sort descending** — Sort the scores in descending order so the highest score is at index 0.

3. **Assign ranks** — Iterate through the sorted scores and assign ranks based on position:
   - Index 0 → "Gold Medal"
   - Index 1 → "Silver Medal"
   - Index 2 → "Bronze Medal"
   - Index i → str(i+1)

4. **Place at original index** — Use the dictionary to place each rank at the athlete's original position in the output array.

---

## Complexity

- **Time:** O(n log n) — dominated by the sort
- **Space:** O(n) — for the dictionary and output array

---

## Code

```python
class Solution():
    def rank(self, score):
        dictionary = {}
        output = [""] * len(score)
        for i in range(len(score)):
            dictionary[score[i]] = i
        score.sort(reverse=True)
        for i in range(len(score)):
            if i == 0:
                output[dictionary[score[i]]] = "Gold Medal"
            elif i == 1:
                output[dictionary[score[i]]] = "Silver Medal"
            elif i == 2:
                output[dictionary[score[i]]] = "Bronze Medal"
            else:
                output[dictionary[score[i]]] = str(i + 1)
        return output


def main():
    score = list(map(int, input("Enter the scores: ").split()))
    s = Solution()
    ranks = s.rank(score)
    print("Ranks are:", ranks)

if __name__ == "__main__":
    main()
```