class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False for _ in target]

        for triplet in triplets:
            # A value above its target can never be reduced by merging.
            if any(triplet[i] > target[i] for i in range(len(target))):
                continue

            # Record each target value supplied by this usable triplet.
            for i in range(len(target)):
                if triplet[i] == target[i]:
                    found[i] = True

        return all(found)
