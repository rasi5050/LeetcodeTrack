class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #sort, find min difference
        arr.sort()
        res=[]
        minAbsDiff=float("+inf")
        for i in range(len(arr)-1):
            minAbsDiff=min(minAbsDiff,arr[i+1]-arr[i])
            
        #sliding window, only nearest elements after sorting can have min absolute val
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minAbsDiff:
                res.append([arr[i],arr[i+1]])
        return res
        
        