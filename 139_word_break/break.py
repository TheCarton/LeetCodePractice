from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]
       
            
s = Solution()            

def example_1():
    r = s.wordBreak("leetcode", ["leet", "code"])
    assert(r)

example_1()