class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count_heap = [-c for c in count.values()]
        
        
        heapq.heapify(count_heap)
        time  = 0
        q = deque()
    
        while count_heap or q:
            time += 1

            if count_heap:
                count = 1 + heapq.heappop(count_heap)
                if count:
                    q.append([count, time+n])
            else:
                time = q[0][1]

            if q and q[0][1] <= time:
                next_time = q.popleft()[0]
                heapq.heappush(count_heap, next_time)

        return time


        
        
