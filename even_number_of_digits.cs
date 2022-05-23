public class Solution {
    public int FindNumbers(int[] nums) {
        // Given an array nums of integers, return how many of them contain an even number of digits.
        int count = 0;
        for (int i = 0; i<nums.Length; i++){
            int length_to_string = Convert.ToString(nums[i]).Length;
            if (length_to_string % 2 == 0){
                count += 1;
            }
        }
        return count; 
    }   
}
