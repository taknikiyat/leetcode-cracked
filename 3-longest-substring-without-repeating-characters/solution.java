class Solution {
    // O(n) time | O(n) space
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> sliding_window_set = new HashSet();
        int left = 0;
        int longest_substring_length = 0;
        for (int right=0; right < s.length() ; right++) {
            while(sliding_window_set.contains(s.charAt(right))) { // // if letter already exists in window
                sliding_window_set.remove(s.charAt(left)); // remove first letter of window
                left += 1; // update pointer for first letter of window
            }
            sliding_window_set.add(s.charAt(right)); // add new letter in window
            longest_substring_length = Math.max(longest_substring_length, sliding_window_set.size()); 
        }
        return longest_substring_length;        
    }
}
