class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        #sort
        arr.sort()
        res=[]
        curMin=float("+inf")
        #minimum absolute difference would be the adjacent elements, sliding window, for new minimum reset and update res
        for i in range(len(arr)-1):
            curDiff=arr[i+1]-arr[i]
            if curDiff<curMin: res=[[arr[i],arr[i+1]]]; curMin=curDiff
            elif curDiff==curMin: res.append([arr[i],arr[i+1]])
        return res
        