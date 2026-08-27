class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        adjacency = [[] for _ in range(n)]
        for source, destination in edges:
            indegree[destination] += 1
            adjacency[source].append(destination)

        queue = deque()
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbour in adjacency[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return result if len(result) == n else []
