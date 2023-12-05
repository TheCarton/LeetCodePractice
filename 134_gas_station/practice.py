from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_total = 0
        running_total = 0
        starting_j = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            net_total += diff
            running_total += diff
            if running_total <= 0:
                running_total = 0
                starting_j = (i + 1) % len(gas)

        if net_total >= 0:
            return starting_j

        return -1


s = Solution()


def example_1():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    r = s.canCompleteCircuit(gas, cost)
    print(r)
    assert (r == 3)


example_1()
