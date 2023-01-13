class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #two sum
        
        def twoSum(j, target):
            map={}
            
            temp=[]
            for i in range(j+1,len(nums)):
                if target-nums[i] in map:
                    temp.append((i, map[target-nums[i]]))
                map[nums[i]]=i
            for i in range(j):
                if target-nums[i] in map:
                    temp.append((i, map[target-nums[i]]))
                map[nums[i]]=i
            return temp
        res=set()
        targetVisited=set()
        # res=[]
        for j,target in enumerate(nums):
            if target in targetVisited:
                continue
            out=twoSum(j, -target)
            for item in out:
                i,k=item
                # res.append((nums[j],nums[i],nums[k]))
                res.add(tuple(sorted((nums[j],nums[i],nums[k]))))
            targetVisited.add(target)
        return res
                