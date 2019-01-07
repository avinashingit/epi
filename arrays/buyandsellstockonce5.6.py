# @Author: Avinash Kadimisetty <avinashingit>
# @Date:   2019-01-07T14:15:35-06:00
# @Email:  kavinash366@gmail.com
# @Project: Elements of Programming Interviews
# @Filename: buyandsellstockonce5.6.py
# @Last modified by:   avinashingit
# @Last modified time: 2019-01-07T14:27:12-06:00
# @License: MIT License

'''
Q: Write a program that takes an array denoting the daily stock price, and
retums the maximum profit that could be made by buying and then selling one
share of that stock. There is no need to buy if a no profit is possible.
'''


def buyandsellstockonce(prices):
    buyprice = prices[0]
    bestprofit, currentprofit = 0, 0
    for i in range(1, len(prices)):
        if prices[i] > buyprice and prices[i] - buyprice > currentprofit:
            currentprofit = prices[i] - buyprice
        else:
            buyprice = prices[i]
            bestprofit = max(bestprofit, currentprofit)
            currentprofit = 0
        bestprofit = max(bestprofit, currentprofit)
    return bestprofit


buyandsellstockonce([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
