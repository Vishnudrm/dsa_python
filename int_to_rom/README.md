# 12. Integer to Roman

**Difficulty:** Medium
**Topics:** Math, String, Greedy

## Problem

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral follows these rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9, use the subtractive form representing one symbol subtracted from the following symbol. For example, 4 is 1 (I) less than 5 (V): IV, and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), and 900 (CM).
- Only powers of ten (I, X, C, M) can be appended consecutively, and at most three times, to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If a symbol needs to be appended four times, use the subtractive form instead.

Given an integer, convert it to a Roman numeral.

## Examples

**Example 1:**
```
Input: num = 3749
Output: "MMMDCCXLIX"
```
Explanation: 3000 → MMM, 700 → DCC, 40 → XL, 9 → IX
Note: 49 is not "1 (I) less than 50 (L)" because the conversion is based on decimal places, not the raw value.

**Example 2:**
```
Input: num = 58
Output: "LVIII"
```
Explanation: 50 → L, 8 → VIII

**Example 3:**
```
Input: num = 1994
Output: "MCMXCIV"
```
Explanation: 1000 → M, 900 → CM, 90 → XC, 4 → IV

## Constraints

- `1 <= num <= 3999`

## Complexity

**Time Complexity:** O(1)
The dictionary has a fixed 13 entries, and since `num` is bounded by the constraint (1 to 3999), the total number of symbols appended is also bounded by a constant, regardless of input size.

**Space Complexity:** O(1)
The output string length is bounded too — the longest possible Roman numeral within the given constraints (3888 → "MMMDCCCLXXXVIII") is 15 characters, so the space used doesn't grow with input in any unbounded way.