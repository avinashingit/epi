# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-05T16:09:25-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: incrementarray5.2.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-05T16:20:52-06:00
# @License: MIT License

'''
Write a program which takes as input an array of digits encoding a nonnegative
decimal integer D and updates the array to represent the integer D + 1. For
example, if the input is (7,2,9) then you should update the array to (1,3,0).
Your algorithm should work even if it is implemented in a langua ge that has
finite-precision arithmetic.
'''


def incrementarray(A):
    A[-1] += 1
    for i in range(len(A)-1, 0, -1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
