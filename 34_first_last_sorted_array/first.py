class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        def search(t):
            left, right = 0, len(nums)
            found = False

            while left < right:
                mid = (left + right) // 2

                if nums[mid] == t:
                    found = True
                if nums[mid] < t:
                    left = mid + 1
                else:
                    right = mid

            return (found, left)

        target_exists, left = search(target)
        if not target_exists:
            return [-1, -1]

        _, right = search(target + 1)

        return [left, right - 1]
