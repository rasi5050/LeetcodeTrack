#idea: do dict of dict, for each key in dict also store the stack, where stack top is the max time till that point==>problem with idea,

#do not optimal solution
"""TLE;correct
class TimeMap:
    def __init__(self):
        self.map=defaultdict(dict)                #key:{time:2}
                                                        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(self.map)
        self.map[key][timestamp]=value
        

    def get(self, key: str, timestamp: int) -> str:
        # print(self.map, key, timestamp)
        if key not in self.map: return ""
        if timestamp in self.map[key]: return self.map[key][timestamp]
        else: 
            for n in range(timestamp-1, -1, -1):
                if n in self.map[key]:
                    return self.map[key][n]
            return ""
"""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

class TimeMap:
    def __init__(self):
        self.map=defaultdict(list)                #key:{time:2}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(self.map)
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # print(self.map, key, timestamp)
        if key not in self.map: return ""
        else:
            # do binary search
            l,r=0,len(self.map[key])-1
            while l<=r:
                mid=(l+r)//2
                currTimestamp=self.map[key][mid][0]
                currValue=self.map[key][mid][1]
                if currTimestamp==timestamp:
                    return currValue
                elif currTimestamp<timestamp:
                    l=mid+1
                elif timestamp<currTimestamp:
                    r=mid-1
                possibleLeftTimestamp=self.map[key][min(l,len(self.map[key])-1)][0]
                possibleRightTimestamp=self.map[key][max(r,0)][0]
                possibleLeftValue=self.map[key][min(l,len(self.map[key])-1)][1]
                possibleRightValue=self.map[key][max(r,0)][1]
                
            if possibleLeftTimestamp<timestamp: return possibleLeftValue
            if possibleRightTimestamp<timestamp: return possibleRightValue
            return ""
        
        
        