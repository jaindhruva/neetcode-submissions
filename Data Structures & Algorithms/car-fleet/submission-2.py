class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time_map = []
        n = len(position)
        for i in range(n):
            pos_time_map.append([position[i], ((target-position[i])/speed[i])])
        
        pos_time_map = sorted(pos_time_map)

        fleet_count = 1
        curr_eta = pos_time_map[n-1][1]
        for i in range (n-2, -1, -1):
            if curr_eta < pos_time_map[i][1]:
                fleet_count += 1
                curr_eta = pos_time_map[i][1]

        return fleet_count
                
        
