class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mp;
        int c = 0;
        for(int i=0;i<nums.size();i++)
        {
            c = target - nums[i];
            if(mp.count(c))
            {
                return {i,mp[c]};
            }
            mp[nums[i]] = i;
        }
        return {-1,-1}; 
    }
};