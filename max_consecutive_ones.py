class Solution:
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
  # Given a binary array nums, return the maximum number of consecutive 1's in the array.
  count = 0
  highest_count = 0
  if len(nums) > 0:
    for i in range(len(nums)):
      if nums[i] == 1:
        count += 1
      else:
        if count > highest_count:
          highest_count = count
          count = 0
  if highest_count > count:
    return highest_count
  else:
    return count
