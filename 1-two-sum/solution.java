// Solution 1: using brute force
// O(n^2) time | O(1) space
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i=0 ; i<nums.length-1; i++) {
            for (int j=i+1 ; j<nums.length; j++) {
                if (nums[i] + nums[j] == target)
                    return new int [] {i, j};
            }
        }
        return null;
    }  
}


// Solution 2: using hash map
// O(n) time | O(n) space
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nums_map = new HashMap<>();
        for (int i=0 ; i<nums.length; i++) {
            if (nums_map.containsKey(target - nums[i])) // if complement of current number exists in map
                return new int[] {nums_map.get(target - nums[i]), i}; // return complement's index and current index
            nums_map.put(nums[i], i); // add current number as key in map with index as value
        }
        return null;
    }  
}
