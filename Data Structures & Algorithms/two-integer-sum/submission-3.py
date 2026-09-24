class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]].append(i) 
            else:
                hmap[nums[i]] = [i]
        
        print(hmap)
        for n in nums:
            if (target - n) in hmap:
                if len(hmap[target - n]) == 1:
                    if hmap[n][0] != hmap[target-n][0]:
                        return [hmap[n][0],hmap[target-n][0]]   
                else:   
                    return [hmap[n][0],hmap[n][1]]      
        
        return [-1,-1]