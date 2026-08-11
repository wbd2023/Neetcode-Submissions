class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front, back = 0, len(nums) - 1

        while front <= back:
            if nums[front] != val:
                front += 1
                continue

            # Swap `val` at `front` with the unchecked value at `back`, pushing `val` to the end.
            # Only move `back` because the value swapped into `front` still needs checking.
            nums[front], nums[back] = nums[back], nums[front]
            back -= 1

        # By the end, `front` points just after all the non-`val` values.
        # Since indices start at 0, its index is also the number of values before it, so there is no need to add 1.
        # Alternatively, return `back + 1`.
        return front
