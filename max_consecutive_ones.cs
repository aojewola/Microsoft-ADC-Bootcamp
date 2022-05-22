public class Solution {
  public int FindMaxConsecutiveOnes(int[] nums) {
  // Given a binary array nums, return the maximum number of consecutive 1's in the array.
    int count = 0;
    int highest_count = 0;
    for (int i = 0; i<nums.Length; i++){
      if (nums[i] == 1){
      count += 1;
      }
      else {
        if (count > highest_count){
        highest_count = count;
        }
        count = 0;
        }
        }
    return highest_count > count? highest_count:count;
    }
}
