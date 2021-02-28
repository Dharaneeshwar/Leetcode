class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, map<int,vector<int>> > m;
        queue<pair<TreeNode*,int>> que,level;
        int index = 0;
        que.push(make_pair(root,0));
        level.push(make_pair(root,0));
        while(!que.empty()){
            auto front = que.front();
            auto curr = level.front();
            if(front.first->left != nullptr){
                que.push(make_pair(front.first->left,front.second-1));
                level.push(make_pair(front.first->left,curr.second+1));
            }
            if(front.first->right != nullptr){
                que.push(make_pair(front.first->right,front.second+1));
                level.push(make_pair(front.first->right,curr.second+1));
            }
            m[front.second][curr.second].push_back(front.first->val);
     
            que.pop();
            level.pop();
        }
       vector<vector<int>> vec(m.size());
        for(pair<int,map<int,vector<int>>> p : m){
            for(pair<int,vector<int>> q : p.second){
              sort(q.second.begin(),q.second.end());
                vec[index].insert(vec[index].end(),q.second.begin(),q.second.end());
            }
            index++;
        }
        return vec;
    }
};