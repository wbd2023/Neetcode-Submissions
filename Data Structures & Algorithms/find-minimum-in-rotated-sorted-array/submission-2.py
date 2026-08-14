class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The array hasn't been rotated, since it's already sorted.
        first, last = nums[0], nums[-1]
        if first < last:
            return first

        # The rotated array is divided into two sorted sections:
        #
        #   Higher section (`first` starts here)  |  Lower section (`last` ends here)
        #   [x, x + 1, ..., maximum]              |  [minimum, ..., x - 2, x - 1]
        #   Every value is >= `first`             |  Every value is < `first`
        #
        # The search finds the boundary between these sections.
        left, right = 0, len(nums) - 1
        while abs(right - left) > 1:
            mid = (left + right) // 2

            print(left, right, mid)

            # `mid` is in the lower section.
            if nums[mid] < first:
                right = mid
                continue

            # `mid` is in the higher section.
            if nums[mid] > first:
                left = mid
                continue

        # `right` is the first value in the lower section.
        return nums[right]
