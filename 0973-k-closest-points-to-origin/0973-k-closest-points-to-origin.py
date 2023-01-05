class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        items=defaultdict(list)
        for x,y in points:
            items[(x**2)+(y**2)].append([x,y])
        # print(items)
        res=[]
        for key in sorted(items.keys()):
            if len(items[key])>1:
                for more in items[key]:
                    res.append(more)
                    k-=1
                    if k==0: return res
            else:
                res.append(*items[key])
                k-=1
                if k==0: return res