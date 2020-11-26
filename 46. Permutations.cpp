// CPP Implementation of Permutation
class Solution {
public:
    vector<vector<int>> result;

    void helper(vector<int>& nums,vector<int>& temp,vector<vector<int>>& result){
        if (nums.size()== 0){
            result.push_back(temp);
            // return;
        }
        for (int i=0;i<nums.size();i++){
            vector<int>::iterator it;
            vector<int> t_nums;
            t_nums.assign(nums.begin(), nums.end()); 
            vector<int> t_temp;
            t_temp.assign(temp.begin(), temp.end()); 
            it = t_nums.begin();
            int temp_value = *(t_nums.begin()+i);
            t_nums.erase(it+i);
            t_temp.push_back(temp_value);
            helper(t_nums,t_temp,result);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp = {};
        helper(nums,temp,result);
        return result;
    }
    
};