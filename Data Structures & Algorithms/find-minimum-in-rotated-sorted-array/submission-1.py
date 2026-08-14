class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Array has not been rotated.
        first, last = nums[0], nums[-1]
        if first < last:
            return first

        # first > last

        left, right = 0, len(nums) - 1
        while abs(right - left) > 1:
            mid = (left + right) // 2

            print(left, right, mid)

            if nums[mid] < first:
                right = mid
                continue

            if nums[mid] > first:
                left = mid
                continue

        return nums[right]
