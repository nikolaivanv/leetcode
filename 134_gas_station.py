import unittest


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start = 0
        steps = 0
        gas_left = 0
        l = len(gas)
        for i in range(l*2):
            if gas_left + gas[i % l] >= cost[i % l]:
                gas_left += gas[i % l] - cost[i % l]
                steps += 1
            else:
                start = i + 1
                gas_left = 0
                steps = 0
            if steps == l:
                return start
        return -1


class TestSolution(unittest.TestCase):   
    def test_1(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        correct_answer = 3
        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), correct_answer)
  
    def test_2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        correct_answer = -1
        solution = Solution()
        self.assertEqual(solution.canCompleteCircuit(gas, cost), correct_answer)
   
    
unittest.main()