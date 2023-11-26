class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palins = []

        def palindrome(sub: str) -> bool:
            return sub == sub[::-1]

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
