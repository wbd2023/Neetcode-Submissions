class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = set()
        dependencies = defaultdict(set)  # course -> prerequisite courses
        dependents = defaultdict(set)    # prerequisite -> dependent courses
        for course, prerequisite in prerequisites:
            courses.update([course, prerequisite])
            dependencies[course].add(prerequisite)
            dependents[prerequisite].add(course)

        queue = deque()
        for course in courses:
            if not dependencies[course]:
                queue.append(course)

        # print(courses)
        # print(dependencies)
        # print(dependents)
        # print(queue)

        completed = set()
        while queue:
            course = queue.pop()
            completed.add(course)

            for dependent in dependents[course]:
                dependencies[dependent].remove(course)

                if not dependencies[dependent]:
                    queue.append(dependent)

        return len(completed) >= numCourses
