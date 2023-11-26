from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=lambda w: len(w))
        prefix = [c for c in shortest_word] 
        for word in strs:
            matching_n = 0
            for (a, b) in zip(prefix, word):
                if a == b:
                    matching_n += 1
                else:
                    break

            del prefix[matching_n:]
            if len(prefix) == 0:
                return ""

        return "".join(prefix)


s = Solution()

def example_1():
    words = ["flower","flow","flight"]
    r = s.longestCommonPrefix(words)
    print(r)


example_1()
