public class Solution {
    public void Rotate(int[] nums, int k) {
        int size = nums.Length;
        if(size == 0 || size ==1) return ;
        k = k % size ; 
        
        reverse(nums, 0 , size-1);
        reverse(nums, 0 , k-1);
        reverse(nums, k , size-1);
    }
    
    public void reverse(int[] arr , int start, int end){
        
        while(start < end){
            int x  = arr[start];
            arr[start] = arr[end];
            arr[end] = x;
            start++;
            end--;
        }
    }
}
