class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        front, back = 0, len(nums) - 1

        while front <= back:
            print(nums, front, back)

            if nums[front] != val:
                front += 1
                continue
            
            # Swap numbers pointed to by `front` and `back`, and move back backwards.
            nums[front], nums[back] = nums[back], val
            back -= 1

        # By the end, `front` should point to the first of the selected values that have been pushed to the end.
        # This includes all the non val values, + the first svalue so theres no need to + 1 to convert 0-based index to 1-bnased.
        # Alternatively, we could do back + 1
        return front
