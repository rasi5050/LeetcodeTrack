class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        """#working code ,commented for optimization 
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
        """
        #status: correct
        #analysis: Time: O(nlogn + 2n)=O(nLogn), Space: O(1)
        
        #optimization: do in one pass Time: O(nLogn + n), Space:O(1) 
        
        #sort, find min difference
        arr.sort()
        res=[]
        minAbsDiff=float("+inf")
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < minAbsDiff:
                minAbsDiff=arr[i+1]-arr[i]
                res=[[arr[i],arr[i+1]]]
            elif arr[i+1]-arr[i]==minAbsDiff:
                res.append([arr[i],arr[i+1]])
        return res
        
        