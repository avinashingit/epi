# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-06T14:08:24-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: advancingarray5.4.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-07T13:48:35-06:00
# @License: MIT License

'''
Q: Write a program which takes an array of n integers, where A[i] denotes the
maximum you can advance from index l, and retums whether it is possible to
advance to the last index starting from the beginning of the array.
'''


def advance(nums):
    max_reach = 0
    i = 0
    while i <= max_reach and max_reach < len(nums)-1:
        max_reach = max(max_reach, nums[i] + i)
        i += 1
    return max_reach >= len(nums)-1
