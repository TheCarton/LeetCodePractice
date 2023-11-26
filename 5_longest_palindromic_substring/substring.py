class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_range = (0, 1)
        for i in range(len(s)):
            left = i - 1
            right = i
            while right < len(s) and s[i] == s[right]:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            best_range = max(best_range, (left + 1, right - 1), key = lambda r: r[1] - r[0])
        return s[best_range[0]:best_range[1]]


s = Solution()
def example_1():
    e1 = "babad"
    r = s.longestPalindrome(e1)
    c = "aba"
    print(r)
    print(c)

def example_2():
    e2 = "cbbd"
    r = s.longestPalindrome(e2)
    c = "bb"
    print(r)
    print(c)


example_1()
example_2()