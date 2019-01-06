# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-05T16:27:55-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: bitaddition5.2.1.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-06T13:39:36-06:00
# @License: MIT License

'''
Q: Write a program which takes as input two strings s and t of bits
encoding binary numbers Bs, and Bt, respectively, and returns a new string of
bits representing the number Bs + Bt.
'''


def addbinary(s, t):
    if len(s) > len(t):
        t = "0"*(len(s)-len(t)) + t
    elif len(s) < len(t):
        s = "0"*(len(t)-len(s)) + s

    carry, output = 0, ""
    for i in range(len(s)-1, -1, -1):
        sums = int(t[i]) + int(s[i]) + carry
        if sums == 2:
            carry, result = 1, 0
        elif sums == 3:
            carry, result = 1, 1
        else:
            carry, result = 0, sums
        output = str(result) + output
    if carry is not 0:
        output = str(carry) + output
    return output
