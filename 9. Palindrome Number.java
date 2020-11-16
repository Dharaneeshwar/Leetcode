// O(n)
class Solution {
    public boolean isPalindrome(int x) {
        if (x<0)
            return false; 
        else{
            int rev=0,dig=0,dup=x;
            while (x){
                dig=x%10;
                rev=rev*10+dig;
                x/=10;
            }
            if (rev==dup){
                return 1;
            }
            else{
                return 0;
            }
            
        }    
    }
}