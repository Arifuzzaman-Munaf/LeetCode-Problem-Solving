public class Solution {
    public int[] PlusOne(int[] digits) {
        int size = digits.Length;
        if(digits[size-1] < 9) {
            digits[size-1]++;
            return digits;
        }
        
        string number = ""+0;
        int carry= 1;
        for(int i = size-2 ; i >= 0 ; i--){
            
            if(digits[i]+carry == 10) {
                number += 0;
                carry = 1;
            }
            else{
                
                number += (digits[i]+carry);
                carry = 0 ;
            }
        }
        
        if(carry == 1) number += 1;
        
        digits = new int[number.Length];
        
        carry = digits.Length - 1 ;
        foreach(var item in number){
            digits[carry--] = (int)item - 48;
        }
        
        return digits;
    }
}
