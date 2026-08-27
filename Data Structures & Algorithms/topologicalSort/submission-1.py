class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        adjancency = defaultdict(list)
        for source, destination in edges:
            indegree[destination] += 1
            adjancency[source].append(destination)

        queue = deque()
        for node in range(n):
            if indegree.get(node, 0) == 0:
                queue.append(node)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbour in adjancency.get(node, []):
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return result if len(result) == n else []
