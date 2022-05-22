class Solution:
    def findNumbers(self, nums: List[int]) -> int:
     # Given an array nums of integers, return how many of them contain an even number of digits.
        count = 0
        for i in range(len(nums)):
            length = len(str(nums[i]))
            if int(length) % 2 == 0:
                count += 1
        return count
                
