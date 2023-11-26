class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        prev = 1
        prev_prev = 1
        for i in range(1, len(s)):
            single = int(s[i])
            double = int(s[i - 1]) * 10 + single
            curr = 0
            if single > 0:
                curr += prev
            if double >= 10 and double <= 26:
                curr += prev_prev
            prev_prev = prev
            prev = curr

        return prev

            

s = Solution()
def example_1(): 
    string = "12"
    correct = 2
    r = s.numDecodings(string)
    print(f"{r}\n{correct}")

def example_2():
    string = "226"
    correct = 3
    r = s.numDecodings(string)
    print(f"{r}\n{correct}")


def example_3():
    string = "06"
    correct = 0
    r = s.numDecodings(string)
    print(f"{r}\n{correct}")


def main():
    example_1()
    example_2()
    example_3()

main()
    