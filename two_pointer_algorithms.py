class Solution:
    def twoSum(self, nums, target):
        # Using two pointer algorithms (assuming nums is a sorted array)
        N = len(nums)
        i, j = 0, N-1
        while i<j:
            current_sum = nums[i] + nums[j]
            if  current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1
            else:
               return [i, j]
                  
