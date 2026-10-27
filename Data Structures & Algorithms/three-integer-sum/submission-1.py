class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        prev = None
        n = len(nums)
        res = set()

        def twoSum(target, indexToSkip):
            mySet = set()
            for i in range(len(nums)):
                if i == indexToSkip:
                    continue
                if target - nums[i] in mySet:
                    arr = [-target, nums[i], target - nums[i]]
                    arr.sort()
                    res.add((arr[0], arr[1], arr[2]))

                mySet.add(nums[i])

        for i in range(n):
            num = nums[i]
            twoSum(-num, i)

        return list(res)
        