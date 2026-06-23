# 3Sum

## Problem Description

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

### Example

#### Input

```text
nums = [-1,0,1,2,-1,-4]
```

#### Output

```text
[[-1,-1,2],[-1,0,1]]
```

---

## Approach

### Brute Force Approach

A straightforward solution is to generate all possible triplets using three nested loops and check whether their sum is equal to zero.

```text
for i
    for j
        for k
            if nums[i] + nums[j] + nums[k] == 0
                store triplet
```

#### Drawbacks

- Time Complexity: `O(n³)`
- Produces duplicate triplets.
- Inefficient for large inputs.

---

## Optimized Approach: Sorting + Two Pointers

The key observation is that after sorting the array, we can efficiently search for pairs using the two-pointer technique.

### Step 1: Sort the Array

Example:

```text
Input:
[-1,0,1,2,-1,-4]

Sorted:
[-4,-1,-1,0,1,2]
```

Sorting allows us to make decisions based on whether the current sum is too large or too small.

---

### Step 2: Fix One Element

Iterate through the array and treat each element as the first element of the triplet.

```text
i = 0 → -4
i = 1 → -1
i = 2 → -1
...
```

To avoid duplicate triplets:

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

---

### Step 3: Use Two Pointers

For each fixed element:

```text
left  = i + 1
right = n - 1
```

Compute:

```text
sum = nums[i] + nums[left] + nums[right]
```

#### Case 1: Sum < 0

The sum is too small.

Move the left pointer to increase the sum.

```python
left += 1
```

---

#### Case 2: Sum > 0

The sum is too large.

Move the right pointer to decrease the sum.

```python
right -= 1
```

---

#### Case 3: Sum == 0

A valid triplet is found.

```python
result.append([nums[i], nums[left], nums[right]])
```

Move both pointers:

```python
left += 1
right -= 1
```

Skip duplicates:

```python
while left < right and nums[left] == nums[left - 1]:
    left += 1

while left < right and nums[right] == nums[right + 1]:
    right -= 1
```

---

## Algorithm

```text
Sort the array

For each element i:
    Skip duplicates

    left = i + 1
    right = n - 1

    While left < right:

        total = nums[i] + nums[left] + nums[right]

        If total < 0:
            left += 1

        Else if total > 0:
            right -= 1

        Else:
            Store triplet

            left += 1
            right -= 1

            Skip duplicate left values
            Skip duplicate right values

Return result
```

---

## Dry Run

### Input

```text
[-1,0,1,2,-1,-4]
```

### Sorted Array

```text
[-4,-1,-1,0,1,2]
```

### Iteration

#### Fixed Element = -4

```text
-4 + (-1) + 2 = -3
```

No valid triplet.

---

#### Fixed Element = -1

```text
-1 + (-1) + 2 = 0
```

Triplet Found:

```text
[-1,-1,2]
```

Move pointers.

---

```text
-1 + 0 + 1 = 0
```

Triplet Found:

```text
[-1,0,1]
```

---

#### Next -1

Duplicate fixed element.

Skipped.

---

### Final Result

```text
[[-1,-1,2],[-1,0,1]]
```

---

## Correct Python Implementation

```python
class Solution:
    def triple(self, array):
        array.sort()
        result = []

        for i in range(len(array) - 2):

            if i > 0 and array[i] == array[i - 1]:
                continue

            left = i + 1
            right = len(array) - 1

            while left < right:

                total = array[i] + array[left] + array[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append(
                        [array[i], array[left], array[right]]
                    )

                    left += 1
                    right -= 1

                    while left < right and array[left] == array[left - 1]:
                        left += 1

                    while left < right and array[right] == array[right + 1]:
                        right -= 1

        return result
```

---

## Complexity Analysis

### Time Complexity

#### Sorting

```text
O(n log n)
```

#### Outer Loop

Runs `n` times.

```text
O(n)
```

#### Two-Pointer Traversal

Each traversal is linear.

```text
O(n)
```

Overall:

```text
O(n²)
```

---

### Space Complexity

Ignoring the output list:

```text
O(1)
```

Including the output:

```text
O(k)
```

where `k` is the number of valid triplets found.

---

## Key Ideas

1. Sort the array first.
2. Fix one element at a time.
3. Use two pointers to find the remaining two elements.
4. Skip duplicate values to avoid repeated triplets.
5. Achieve an optimal time complexity of `O(n²)` instead of `O(n³)`.

This is the standard optimal solution for the 3Sum problem.