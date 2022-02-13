class Solution {
public:
    // O(n) time | O(n) space
    int lengthOfLongestSubstring(string s) {
        unordered_set <char> sliding_window_set;
        int left = 0;
        int longest_substring_length = 0;
        for (int right=0; right < s.length() ; right++) {
            while(sliding_window_set.find(s[right]) != sliding_window_set.end()) { // if letter already exists in window
                sliding_window_set.erase(s[left]); // remove first letter of window
                left += 1; // update pointer for first letter of window
            }
            sliding_window_set.insert(s[right]); // add new letter in window
            int size = sliding_window_set.size();
            longest_substring_length = std::max(longest_substring_length, size); 
        }
        return longest_substring_length;                
    }     
};
