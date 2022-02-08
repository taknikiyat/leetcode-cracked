// Solution 1: using brute force
// O(n^2) time | O(1) space
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size() - 1; i++) {
            for(int j = i+1; j < nums.size(); j++) {
                if(nums[i] + nums[j] == target)
                    return vector<int> {i, j};
            }
        }
        return {};
    }
};


// Solution 2: using hash map
// O(n) time | O(n) space
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> nums_map;
        for(int i = 0; i < nums.size(); i++){
            if(nums_map[target-nums[i]] > 0) // if complement of current number exists in map
                return{nums_map[target-nums[i]] - 1, i}; // return complement's index and current index
            nums_map[nums[i]] = i+1; // add current number as key in map with index as value
        }
        return {};
    }
};
