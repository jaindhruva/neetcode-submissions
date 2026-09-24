class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        indegree = [0]*numCourses

        for main_course,prereq_course in prerequisites:
            prereq_map[main_course].append(prereq_course)
            indegree[prereq_course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            size = len(q)
            for i in range(size):
                course = q.popleft()
                finished += 1
                for prereq in prereq_map[course]:
                    indegree[prereq] -= 1
                    if indegree[prereq] == 0:
                        q.append(prereq)


        return finished==numCourses