class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 1
        n = len(fruits)
        if n == 1:
            return n
        count_map = {fruits[0]: 1}
        max_fruits = 1
        while r < n:

            # increase window size
            if fruits[r] in count_map:
                count_map[fruits[r]] += 1
            else:
                count_map[fruits[r]] = 1
            
            # pop if needed
            while len(count_map) > 2:
                count_map[fruits[l]] -= 1
                if count_map[fruits[l]] == 0:
                    count_map.pop(fruits[l])
                l += 1

            max_fruits = max(max_fruits, r-l+1)
            r += 1


        return max_fruits