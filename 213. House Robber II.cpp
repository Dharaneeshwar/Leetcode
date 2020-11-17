// Dynamic Programming; Time Complexity: O(2(n-1)) ; (0 ms) ; Space Complexity : O(1) (Constant Space)

class Solution {
public:
    int rob_classic(vector<int>& n,int start,int end){
        int prev = 0,curr = 0;
        for (int i=start;i<=end;i++){
            int temp = max(prev+n[i],curr);
            prev = curr;
            curr = temp;
        }
        return curr;
    }
    int rob(vector<int>& nums) {
        int len = nums.size();
        if (len == 0)
            return 0;
        if (len == 1)
            return nums[0];
        return max(rob_classic(nums,0,len-2),rob_classic(nums,1,len-1));
    }
};