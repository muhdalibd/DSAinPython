"""
    Count digits
        Given a number n, return the count of digits in this number.
    Example:
        Input: n = 1567
        Output: 4
        Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.
"""
import math
num = int(input("Enter a number: "))
# cnt_digit = 0
# while num != 0:
#     digit = num % 10
#     cnt_digit += 1
#     num = num // 10
cnt_digit = round(math.log10(num) + 1)
print(f"The number has {cnt_digit} digits.")
