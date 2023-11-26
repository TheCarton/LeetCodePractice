from typing import List
from collections import defaultdict
       
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return [w for w in anagrams.values()]
       
s = Solution()

def example_1():
    e = ["eat","tea","tan","ate","nat","bat"]
    c = [["bat"],["nat","tan"],["ate","eat","tea"]]
    r = s.groupAnagrams(e)
    print(r)
    print(c)




example_1()