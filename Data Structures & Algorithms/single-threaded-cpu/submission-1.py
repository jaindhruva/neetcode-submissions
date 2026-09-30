class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        
        res, minHeap = [], []
        time, i = tasks[0][0], 0

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0] :
                # there are valid tasks available, add them to minHeap
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]]) # proc time, index
                i += 1
            if minHeap:
                # pop the task and advance the time by proc time needed
                task = heapq.heappop(minHeap)
                res.append(task[1])
                time += task[0]
            else:
                # closest available task
                time = tasks[i][0]

        return res
        