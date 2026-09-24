class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.timeMap[key]
        l, r = 0, len(val_list)-1
        res = ''
        while l<=r:
            m = l + (r-l)//2
            if val_list[m][1] == timestamp:
                return val_list[m][0]
            if val_list[m][1] <= timestamp:
                res = val_list[m][0]
                l = m+1
            else:
                r = m-1

        return res
        
