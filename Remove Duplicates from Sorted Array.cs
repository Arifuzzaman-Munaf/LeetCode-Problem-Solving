public class Solution {
    public int RemoveDuplicates(int[] nums) {
      if(nums.Length == 0 || nums.Length == 1) return nums.Length;
      int key = 0;
      for(int i =0 ; i<nums.Length-1; i++){
          
          if(nums[i] != nums[i+1]) nums[key++] = nums[i];
      }
        
       nums[key++] = nums[nums.Length-1];
       return key ;  
    }
}
