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
        elif timestamp < self.map[key][0][0]: return ""          #all the values in the list are higher than the current timestamp
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
                
                #left value is not required because if not target, we want a value which is less than target, so right value will be the one who is trying to match the target from higher value to lower value, so when the loop breaks right value will be the highest value near to target
            possibleRightTimestamp=self.map[key][max(r,0)][0]
            possibleRightValue=self.map[key][max(r,0)][1]
                
            if possibleRightTimestamp<timestamp: return possibleRightValue
            return ""
        
     #status: correct; took 4hours with the help(https://leetcode.com/problems/time-based-key-value-store/solution/)
     #Analysis: Time O(N*LogM), Space O(N)   
        #ref: 2/7/2023P2:track1-cpGrind75;Day103/104;doLeetcodeBlind75-3q/day-16/45Q:completeOn2/15/2023-Day11/15,collateQuestionPatternIntoCategoriesAndTemplaye-Day2/3:(addWordDescriptionOnceProblemIsSolved)1.(timeBasedKeyValueStoreTimed25Mins)-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.(accountsMergeTimed25Mins)-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.implement-x1pomo(8:00-8:30),6.sortColorsTimed25Mins-x1pomo(8:30-9:00),7.implement-x1pomo(9:00-9:30),8.wordBreakTimed25Mins-x1pomo(9:30-10:00),9.applyInternships(1.https://ups-2022.runmytests.com/job/atlanta/finance-and-accounting-analytics-summer-2023-intern/1187/43530455504,2.https://ups-2022.runmytests.com/job/parsippany/coop-engineering-major-post-grad-hybrid-nj/1187/43537660080,3.https://ups-2022.runmytests.com/job/atlanta/communications-analytics-summer-2023-intern/1187/43537624848,4.https://ups-2022.runmytests.com/job/lutherville-timonium/coop-engineering-major-junior/1187/43537645072,5.https://ups-2022.runmytests.com/job/lutherville-timonium/coop-engineering-major-junior/1187/43537645088)-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        
        
        