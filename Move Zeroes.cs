public class Solution {
    public void MoveZeroes(int[] nums) {
        int size = nums.Length;
        if(size == 1) return;
        
        int index= 0;
        foreach(int i in nums){
            if( i != 0){
                nums[index++] = i;
            }
        }
        
        for(int i = index ; i<size; i++){
            nums[i] = 0;
        }
        
    }
}
