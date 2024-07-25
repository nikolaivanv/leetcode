import unittest

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = len(prices)
        profit = 0
        for i in range(1,l):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff
        return profit



class TestSolution(unittest.TestCase):   
    def test_1(self):
        prices = [7,1,5,3,6,4]
        profit_correct = 7
        solution = Solution()
        profit_calc = solution.maxProfit(prices)
        self.assertEqual(profit_calc, profit_correct)
   
    def test_2(self):
        prices = [1,2,3,4,5]
        profit_correct = 4
        solution = Solution()
        profit_calc = solution.maxProfit(prices)
        self.assertEqual(profit_calc, profit_correct)
        
    def test_3(self):
        prices = [7,6,4,3,1]
        profit_correct = 0
        solution = Solution()
        profit_calc = solution.maxProfit(prices)
        self.assertEqual(profit_calc, profit_correct) 
    
unittest.main()