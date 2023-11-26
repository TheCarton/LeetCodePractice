from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost, start_i, curr_gas = 0, 0, 0, 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]

            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                start_i = (i + 1) % len(gas)
                curr_gas = 0

        if total_gas < total_cost:
            return -1
        else:
            return start_i



s = Solution()

def example_1():
    g = [1,2,3,4,5]
    c = [3,4,5,1,2]
    r = s.canCompleteCircuit(g, c)
    assert(r == 3)

def example_2():
    g = [2, 3, 4]
    c = [3, 4, 3]
    r = s.canCompleteCircuit(g, c)
    assert(r == -1)

def fail_1():
    g = [5,8,2,8]
    c = [6,5,6,6]
    r = s.canCompleteCircuit(g, c)
    assert(r == 3)

fail_1()
example_1()
example_2()