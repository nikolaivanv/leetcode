import unittest


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
            suffix.append(suffix[i-1] * nums[-i])
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[-i-1]
        return nums


class TestSolution(unittest.TestCase):   
    def test_1(self):
        nums = [1,2,3,4]
        correct_answer = [24,12,8,6]
        solution = Solution()
        self.assertTrue(solution.productExceptSelf(nums) == correct_answer)
  
   
    
unittest.main()