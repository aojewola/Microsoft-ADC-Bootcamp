class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
        new_arr = list()
        for i in range(len(nums)):
            new_arr.append((nums[i]) * (nums[i]))
        return sorted(new_arr)
        
