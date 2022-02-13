class Solution(object):
    # O(n) time | O(n) space
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sliding_window_set = set()
        left = 0
        longest_substring_length = 0
        for right in range(len(s)):
            while s[right] in sliding_window_set: # if letter already exists in window
                sliding_window_set.remove(s[left]) # remove first letter of window
                left += 1 # update pointer for first letter of window
            sliding_window_set.add(s[right]) # add new letter in window
            longest_substring_length = max(longest_substring_length, len(sliding_window_set))
        return longest_substring_length
