class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            # Build the new subsets before modifying result:
            # 1. "for subset in result" reads each existing subset.
            # 2. "[num]" turns num into a one-element list.
            # 3. "subset + [num]" concatenates the two lists:
            #       subset = [1, 2], num = 3
            #       [1, 2] + [3] -> [1, 2, 3]
            #    This creates a new list without modifying subset.
            # 4. The surrounding comprehension collects all the new subsets
            #    into a separate outer list.
            # 5. Once that list is complete, "+=" extends result with each
            #    new subset while preserving the existing subsets:
            #       result = [[], [1]]
            #       new subsets = [[2], [1, 2]]
            #       result += [[2], [1, 2]]
            #       result -> [[], [1], [2], [1, 2]]
            result += [subset + [num] for subset in result]

        return result
