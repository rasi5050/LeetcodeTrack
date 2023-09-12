class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # mTemp=nTemp=0
        # tempArray=[]
        # while (mTemp<m and nTemp<n):
        #     if nums1[mTemp]<=nums2[nTemp]:
        #         tempArray.append(nums1[mTemp])
        #         mTemp+=1
        #     else:
        #         tempArray.append(nums2[nTemp])
        #         nTemp+=1
        # if (mTemp<m):
        #     tempArray.extend(nums1[mTemp:])
        # else:
        #     tempArray.extend(nums2[nTemp:])
        # for i in range(m+n):
        #     nums1[i]=tempArray[i]
        
        #optimal method
        i,j,k=m-1,n-1,m+n-1
        
        if j==-1:
            return

            
        while (j>-1 and k>-1):
            if i>-1 and nums1[i] > nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
            
        
                
        