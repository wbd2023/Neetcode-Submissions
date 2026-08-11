class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            # Build the new subsets before modifying result:
            # 1. "for subset in result" reads each existing subset.
            # 2. "[num]" turns num into a one-element list.
            # 3. "subset + [num]" concatenates those lists, creating a new
            #    subset without modifying the original subset.
            # 4. The surrounding comprehension collects all these new subsets
            #    into a separate list.
            # 5. Only after that list is complete does "+=" extend result with
            #    its elements, preserving the existing subsets as well.
            result += [subset + [num] for subset in result]

        return result
