import unittest

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l = len(nums)
        k = l
        i = 0
        j = 0
        while i + j < l:
            if nums[i] == val:
                k = k - 1
                nums[i] = nums[l-j-1]
                nums[l-j-1] = val
                j = j + 1
            else:
                i = i + 1
        return k
        
class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,9,3,9,9,6]
        solution = Solution()
        k = solution.removeElement(nums, 9)
        self.assertEqual(k, 3)
        self.assertEqual(sorted(nums[:k]), [1,3,6])
        
    def test_2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        solution = Solution()
        k = solution.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0,0,1,3,4])
        
        
unittest.main()