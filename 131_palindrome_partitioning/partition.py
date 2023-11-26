from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palins = []
        def palindrome(s) -> bool:
            return s == s[::-1]
        def dfs(i, curr):
            if i == len(s):
                palins.append(curr)
                return
            for j in range(i, len(s)):
                part = s[i:j + 1]
                if palindrome(part):
                    dfs(j + 1, curr + [part])

        dfs(0, [])
        return palins

s = Solution()

def example_1():
    e1 = "aab"
    c = [["a","a","b"],["aa","b"]]
    r = s.partition(e1)
    print(c)
    print(r)

example_1()