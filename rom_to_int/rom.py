# Problem:
# Given a Roman numeral string, convert it into its corresponding integer value.
#
# Roman Numerals:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# Normally, Roman numerals are written from largest to smallest and their
# values are added together.
#
# Examples:
# III    = 1 + 1 + 1 = 3
# LVIII  = 50 + 5 + 1 + 1 + 1 = 58
#
# Special Cases (Subtractive Notation):
# When a smaller numeral appears before a larger numeral, its value is
# subtracted instead of added.
#
# IV = 5 - 1 = 4
# IX = 10 - 1 = 9
# XL = 50 - 10 = 40
# XC = 100 - 10 = 90
# CD = 500 - 100 = 400
# CM = 1000 - 100 = 900
#
# Approach:
# 1. Store the Roman numeral symbols and their corresponding integer values
#    in a dictionary for O(1) lookup.
# 2. Traverse the Roman numeral from right to left using reversed().
# 3. Keep track of the previous numeral's value.
# 4. If the current value is less than the previous value, subtract it
#    (handles cases like IV, IX, XL, XC, CD, CM).
# 5. Otherwise, add the current value to the result.
# 6. Update the previous value after each iteration.
# 7. The final accumulated result is the integer representation.

rom_num=list(input("enter the roman number: "))
print(rom_num)

roman={"I":1,
       "V":5,
       "X":10,
       "L":50,
       "C":100,
       "D":500,
       "M":1000}

integer=0
prev=0

for char in reversed(rom_num):
    curr=roman[char]

    if curr < prev:
        integer -= curr
    else:
        integer += curr

    prev=curr

rom_num="".join(rom_num)

print("the integer corresponding to", rom_num, "is", integer)

# Time Complexity: O(n)
# n = length of the Roman numeral string.
# We traverse the string exactly once.
#
# Space Complexity: O(1)
# The Roman numeral dictionary contains a fixed number of entries (7).
# Only a few extra variables are used regardless of input size.
