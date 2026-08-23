class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        dependents = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            indegree[course] += 1
            dependents[prerequisite].append(course)

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []
        while queue:
            course = queue.popleft()
            order.append(course)

            for dependent in dependents[course]:
                indegree[dependent] -= 1

                if indegree[dependent] == 0:
                    queue.append(dependent)

        return order if len(order) == numCourses else []
