class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        current = {0}

        for num in nums:
            for state in current.copy():
                candidate = state + num
                if candidate > half:
                    continue

                if candidate == half:
                    return True

                current.add(candidate)

        return False
