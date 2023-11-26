class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = dict()
        max_len = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in seen and seen[c] >= left:
                left = seen[c] + 1

            max_len = max(max_len, right + 1 - left)
            seen[c] = right

        return max_len
