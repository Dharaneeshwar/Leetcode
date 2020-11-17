// Classic recursion <Time Limit Exceeded>

class Solution
{
public:
    int max(int a, int b)
    {
        return a > b ? a : b;
    }
    int rob_house(vector<int> &nums, int len, int i, int money)
    {
        if (i >= len)
        {
            return money;
        }
        return max(rob_house(nums, len, i + 1, money), rob_house(nums, len, i + 2, money + nums[i]));
    }
    int rob(vector<int> &nums)
    {
        return rob_house(nums, nums.size(), 0, 0);
    }
};

// Dynamic Programming; Time Complexity: O(n) ; (0 ms) ; Space Complexity : O(n) 

class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size();
        if (len==0){
            return 0;
        }
        if (len==1){
            return nums[0];
        }
        int arr[len];
        arr[0] = nums[0];
        arr[1] = max(nums[0],nums[1]);
        for (int i=2;i<len;i++){
            arr[i] = max(arr[i-2]+nums[i],arr[i-1]);
        }
        return arr[len-1];
    }
};

// Dynamic Programming; Time Complexity: O(n) ; (0 ms) ; Space Complexity : O(1) (Constant Space)

class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size();
        if (len==0){
            return 0;
        }
        if (len==1){
            return nums[0];
        }
        int prev = 0,curr = 0;
        for (int i=0;i<len;i++){
            int temp = max(prev+nums[i],curr);
            prev = curr;
            curr = temp;
        }
        return curr;
    }
};