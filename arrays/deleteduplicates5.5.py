# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-07T13:48:55-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: deleteduplicates5.5.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-07T14:15:26-06:00
# @License: MIT License

'''
Q: Write a program which takes as input a sorted array and updates it so that
all duplicates have been removed and the remaining elements have been shifted
left to fill the emptied indices. Return the number of valid elements.
'''


def removeDuplicates(nums):
    last_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[last_index] = nums[i]
            last_index += 1
    return nums
