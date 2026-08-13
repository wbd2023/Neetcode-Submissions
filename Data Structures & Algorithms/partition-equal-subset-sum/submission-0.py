class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        current = {0}

        for num in nums:
            updated = set()

            for state in current:
                updated.add(state)

                state = state + num
                if state > half:
                    continue

                elif state == half:
                    return True

                else:
                    updated.add(state)

            print(num)
            print(current)
            print(updated)
            print()

            current = updated

        return False
