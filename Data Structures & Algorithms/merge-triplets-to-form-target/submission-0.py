class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False for _ in target]

        for triplet in triplets:
            usable, find = True, [False for _ in target]

            for i in range(len(target)):
                if triplet[i] > target[i]:
                    usable = False
                    break
                
                elif triplet[i] == target[i]:
                    find[i] = True
                    continue

                else:
                    pass

            if not usable:
                continue

            found = [found[i] or find for i, find in enumerate(find)]

        return all(found)
