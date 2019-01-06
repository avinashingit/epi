# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-05T01:35:11-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: parity4.1.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-05T15:10:48-06:00
# @License: MIT License

'''
Q: How would you compute the parity of a very large number of 64-bit words?
'''


def bruteforce(num):
    '''
    Method:
    Keep check if the last bit is 1 or not and shift the number by 1 bit
    until 0. Parity is 0 if even bits else 1.

    Time Complexity: O(n) - n: number of bits
    Space Complexity: O(1)
    '''
    result = 0
    while num:
        result ^= num & 1
        num >>= 1
    return result


def firstbest(num):
    '''
    Method:
    x & x-1 removes the least significant 1 bit. Keep repeating until 0 and
    find the parity.

    Time Complexity: O(k) - k: number of 1 bits
    Space Complexity: O(1)
    '''
    result = 0
    while num:
        result ^= 1
        num &= num - 1
    return result
