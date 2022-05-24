public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Using 2 pointer algorithms 
        int left, right;
        left = 0;
        right = (nums.Length) - 1;
        while (left < right){
            int current_sum = nums[left] + nums[right];
            if (current_sum < target){
                left += 1;
            }
            else if (current_sum > target) {
                right -= 1;
            }
            else{
                int [] res = new int[]{left, right};
                return res;
            }
        }
        return new int []{-1, -1};
    }
}
