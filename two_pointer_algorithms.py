#2 Pointer
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
                  
# Naive Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using two pointer algorithms
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                current_sum = nums[i] + nums[j]
                if current_sum == target:
                    return [i, j]
           
