import max_subarray

def test_ex1():
    s = max_subarray.Solution()
    n = [-2,1,-3,4,-1,2,1,-5,4]
    correct = 6
    assert(s.maxSubArray(n) == correct)
    