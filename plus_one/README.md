# Plus One Problem in Python

## Problem Description

Given a non-negative integer represented as an array of digits, increment the integer by one and return the resulting array of digits.

### Example 1

```text
Input:  [1, 2, 3]
Output: [1, 2, 4]
```

Explanation:

```text
123 + 1 = 124
```

### Example 2

```text
Input:  [4, 3, 2, 1]
Output: [4, 3, 2, 2]
```

Explanation:

```text
4321 + 1 = 4322# Plus One Problem in Python

## Problem Description

Given a non-negative integer represented as an array of digits, increment the integer by one and return the resulting array of digits.

### Example 1

```text
Input:  [1, 2, 3]
Output: [1, 2, 4]
```

Explanation:

```text
123 + 1 = 124
```

### Example 2

```text
Input:  [4, 3, 2, 1]
Output: [4, 3, 2, 2]
```

Explanation:

```text
4321 + 1 = 4322
```

### Example 3

```text
Input:  [9, 9, 9]
Output: [1, 0, 0, 0]
```

Explanation:

```text
999 + 1 = 1000
```

---

## Solution Approach

The solution converts the list of digits into a single integer, increments the integer by one, and then converts the result back into a list of digits.

### Algorithm

1. Initialize a variable `num` to store the integer value.
2. Traverse the digit array.
3. Construct the integer using:

```python
num = num * 10 + digit
```

4. Increment the integer by one.
5. Convert the updated integer into a string.
6. Convert each character back into an integer and store it in a list.
7. Return the resulting list.

### Implementation

```python
class Solution:
    def plus(self, numb):
        num = 0

        for d in numb:
            num = num * 10 + d

        num += 1

        return [int(x) for x in str(num)]


def main():
    num = int(input("Enter the number: "))

    numb = [int(x) for x in str(num)]

    print("Digits:", numb)

    s = Solution()

    plus_one = s.plus(numb)

    print("After adding one:", plus_one)

    number = int("".join(map(str, plus_one)))

    print("Final number is:", number)


if __name__ == "__main__":
    main()
```

---

## Dry Run

Input:

```text
123
```

Digit Array:

```text
[1, 2, 3]
```

Building Number:

```text
num = 0
num = 0 × 10 + 1 = 1
num = 1 × 10 + 2 = 12
num = 12 × 10 + 3 = 123
```

Add One:

```text
123 + 1 = 124
```

Convert Back:

```text
"124" → [1, 2, 4]
```

Output:

```text
Final number is: 124
```

---

## Time Complexity

Let `n` be the number of digits.

### Building the Number

```text
O(n)
```

### Converting Back to List

```text
O(n)
```

### Total Time Complexity

```text
O(n)
```

---

## Space Complexity

The resulting digit array stores `n` digits.

```text
O(n)
```

---

## Key Learning Points

* Converting a digit array to an integer can be done using:

```python
num = num * 10 + digit
```

* List comprehensions provide a concise way to convert characters back into integers.
* This approach is simple and intuitive for understanding the problem.
* For very large digit arrays, an in-place carry-propagation approach is preferred because it avoids integer conversion and handles arbitrarily large numbers efficiently.

```

### Example 3

```text
Input:  [9, 9, 9]
Output: [1, 0, 0, 0]
```

Explanation:

```text
999 + 1 = 1000
```

---

## Solution Approach

The solution converts the list of digits into a single integer, increments the integer by one, and then converts the result back into a list of digits.

### Algorithm

1. Initialize a variable `num` to store the integer value.
2. Traverse the digit array.
3. Construct the integer using:

```python
num = num * 10 + digit
```

4. Increment the integer by one.
5. Convert the updated integer into a string.
6. Convert each character back into an integer and store it in a list.
7. Return the resulting list.

### Implementation

```python
class Solution:
    def plus(self, numb):
        num = 0

        for d in numb:
            num = num * 10 + d

        num += 1

        return [int(x) for x in str(num)]


def main():
    num = int(input("Enter the number: "))

    numb = [int(x) for x in str(num)]

    print("Digits:", numb)

    s = Solution()

    plus_one = s.plus(numb)

    print("After adding one:", plus_one)

    number = int("".join(map(str, plus_one)))

    print("Final number is:", number)


if __name__ == "__main__":
    main()
```

---

## Dry Run

Input:

```text
123
```

Digit Array:

```text
[1, 2, 3]
```

Building Number:

```text
num = 0
num = 0 × 10 + 1 = 1
num = 1 × 10 + 2 = 12
num = 12 × 10 + 3 = 123
```

Add One:

```text
123 + 1 = 124
```

Convert Back:

```text
"124" → [1, 2, 4]
```

Output:

```text
Final number is: 124
```

---

## Time Complexity

Let `n` be the number of digits.

### Building the Number

```text
O(n)
```

### Converting Back to List

```text
O(n)
```

### Total Time Complexity

```text
O(n)
```

---

## Space Complexity

The resulting digit array stores `n` digits.

```text
O(n)
```

---

## Key Learning Points

* Converting a digit array to an integer can be done using:

```python
num = num * 10 + digit
```

* List comprehensions provide a concise way to convert characters back into integers.
* This approach is simple and intuitive for understanding the problem.
* For very large digit arrays, an in-place carry-propagation approach is preferred because it avoids integer conversion and handles arbitrarily large numbers efficiently.
