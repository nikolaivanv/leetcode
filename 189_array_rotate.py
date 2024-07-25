import unittest

class Solution:
    def revert(self, nums: list[int], start: int, end: int) -> None:
        for i in range((end - start) // 2):
            a = nums[start + i]
            nums[start + i] = nums[end - i - 1]
            nums[end - i - 1] = a
        
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        k = k % l
        if k == 0:
            return
        l = len(nums)
        print("start:", nums)
        self.revert(nums,0,l-k)
        print("revert the first part:", nums)
        self.revert(nums,l-k,l)
        print("revert the second part:", nums)
        self.revert(nums,0,l)
        print("revert whole:", nums)


class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        k = k % l
        if k == 0:
            return
        j = 0
        for i in range(l):
            print(f"{nums[:-k]}   {nums[-k:]} | i={i} | j={j}")
            if (i > l - k) and (j == 0):
                break
            a = nums[i]
            nums[i] = nums[l-k+j]
            nums[l-k+j] = a
            if j < k - 1:
                j = j + 1
            else:
                if i < l - k:
                    j = 0


class Solution1:
    def rotate_by_one(self, nums: list[int]) -> None:
        l = len(nums)
        for i in range(1,l):
            a = nums[-i-1]
            nums[-i-1] = nums[-i]
            nums[-i] = a
    
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            self.rotate_by_one(nums)
        
    
class TestSolution(unittest.TestCase):
   
    def test_rotate_by_one(self):
        nums = [1,2,3,4,5,6,7]
        k = 1
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [7,1,2,3,4,5,6])
    
    def test_1(self):
        nums = [1,2,3,4, 5,6,7]
        k = 3
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [5,6,7,1,2,3,4])
    
    def test_2(self):
        nums = [-1,-100,3,99]
        k = 2
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [3,99,-1,-100])
        
    def test_3(self):
        nums = [1,2]
        k = 0
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [1,2])
        
    def test_4(self):
        nums = [1,2,3]
        k = 4
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [3,1,2])
        
    def test_5(self):
        nums = [1,2,3,4,5,6]
        k = 4
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [3,4,5,6,1,2])
        
        
    def test_6(self):
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        k = 38
        solution = Solution()
        solution.rotate(nums, k)
        self.assertEqual(nums, [17,18,19,20,21,22,23,24,25,26,27,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    
unittest.main()