class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = [0] * numCourses                  # course -> prerequisite courses
        dependents = [set() for _ in range(numCourses)]  # prerequisite -> dependent courses

        for course, prerequisite in prerequisites:
            dependencies[course] += 1
            dependents[prerequisite].add(course)

        queue = deque()
        for course in range(numCourses):
            if not dependencies[course]:
                queue.append(course)

        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1

            for dependent in dependents[course]:
                dependencies[dependent] -= 1

                if not dependencies[dependent]:
                    queue.append(dependent)

        return completed == numCourses
