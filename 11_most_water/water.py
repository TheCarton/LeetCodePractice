class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best_area = 0
        while left < right:
            length = right - left

            new_height = height[left]
            if height[left] < height[right]:
                left += 1
            else:
                new_height = height[right]
                right -= 1

            new_area = new_height * length
            best_area = max(new_area, best_area)

        return best_area
