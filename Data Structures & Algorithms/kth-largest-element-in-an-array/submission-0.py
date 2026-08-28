class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minimums = []

        for num in nums:
            if len(minimums) < k:
                heapq.heappush(minimums, num)
                continue

            if num > minimums[0]:
                heapq.heappop(minimums)
                heapq.heappush(minimums, num)
                continue

        return minimums[0]
