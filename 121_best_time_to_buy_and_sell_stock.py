import unittest

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = len(prices)
        profit = 0
        cur_profit = 0
        lowest_price = prices[0]
        for i in range(1,l):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            cur_profit = prices[i] - lowest_price
            if cur_profit > profit:
                profit = cur_profit
        return profit



class TestSolution(unittest.TestCase):   
    def test_1(self):
        prices = [7,1,5,3,6,4]
        profit_correct = 5
        solution = Solution()
        profit_calc = solution.maxProfit(prices)
        self.assertEqual(profit_calc, profit_correct)
   
    def test_2(self):
        prices = [7,6,4,3,1]
        profit_correct = 0
        solution = Solution()
        profit_calc = solution.maxProfit(prices)
        self.assertEqual(profit_calc, profit_correct) 
    
unittest.main()