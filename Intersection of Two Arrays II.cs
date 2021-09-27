public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        
        
        
        if(nums1.Length > 1) Array.Sort(nums1);
        if(nums2.Length > 1) Array.Sort(nums2);
        
        
        List<int> array = new List<int>();
        int i =0, j= 0;
        while(i < nums1.Length && j < nums2.Length){
            if(nums1[i] > nums2[j]) j++;
            else if(nums1[i] < nums2[j]) i++;
            else {
                array.Add(nums1[i]);
                i++;
                j++;
                
            }
        }
        return array.ToArray() ;
    
    }
}
