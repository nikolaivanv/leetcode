import unittest

class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1.copy()
        i = 0
        j = 0
        k = 0
        while  k < m + n:
            if i < m and j < n:
                if (nums1_copy[i] < nums2[j]):
                    nums1[k] = nums1_copy[i]
                    i = i + 1
                else:
                    nums1[k] = nums2[j]
                    j = j + 1
            else:
                if i >= m:
                    nums1[k] = nums2[j]
                    j = j + 1
                else:
                    nums1[k] = nums1_copy[i]
                    i = i + 1
            k = k + 1
        
# The test based on unittest module
class TestSolution(unittest.TestCase):
    def test_equal_length_1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        solution = Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,2,3,5,6])
        
    def test_equal_length_2(self):
        nums1 = [1,5,7,0,0,0]
        m = 3
        nums2 = [2,3,6]
        # [1,5,7]
        # [2,3,6]
        
        # [1,2,5,6,7]
        n = 3
        solution = Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3,5,6,7])
    
    def test_first_is_longer_1(self):
        nums1 = [1,3,5,5,0,0,0]
        m = 4
        nums2 = [2,4,6]
        n = 3
        solution = Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3,4,5,5,6])
        
        
    def test_second_is_longer_1(self):
        nums1 = [1,3,8,0,0,0,0]
        m = 3
        nums2 = [2,5,6,9]
        n = 4
        solution = Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1,2,3,5,6,8,9])
 
#if __name__ == '__main__':
unittest.main()