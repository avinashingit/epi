# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-07T14:41:08-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: longestsubarray5.6.1.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-07T14:49:26-06:00
# @License: MIT License

'''
Q: Write a program that takes an array of integers and finds the length of a
longest subarray all of whose entries are equal.
'''


def longestsubarray(nums):
    if not nums or len(nums) == 0:
        return 0
    l, si, ei = 1, 0, 0
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            ei = i
        else:
            l = max(l, ei - si + 1)
            si, ei = i, i
    return l
