#intuition: from neetcode youtube solution(https://www.youtube.com/watch?v=7ABFKPK2hD4)
#half help form neetcode youtube solution
#idea: node with key, val, prev, next
#sentinal left(pointing to least recently used), right pointer(pointing to most recently used)
#helper functions: remove and insert
#hashmap : maps to key to node

class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        #initially wire them to each other
        self.left.next, self.right.prev=self.right, self.left
    def remove(self, node):
        #place holder
        prev, next = node.prev, node.next
        prev.next, next.prev =next, prev
    
    def insert(self, node):
        #place holder
        prev, next= self.right.prev, self.right
        prev.next=next.prev=node
        node.prev, node.next= prev, next
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            #since access, make it most recent, ie. remove and insert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key]=newNode
        #check capacity
        if len(self.cache)>self.capacity:
            #remove lru
            node=self.left.next
            del self.cache[node.key]
            self.remove(node)
            
    #status: correct
    #analysis: time O(1), each operation is constant time operation
    #space: O(capacity), stores values in hashMap+linkedList  max upto val of capacity
    #ref:11/21/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day44/44:1.doOnSunday:mathWorks-lastDate21 Nov 2022 10:39 AM EST (America - New York)-105MinutesAsperHackerRank(90Mins,expected60MinsAsPerMathworks):doOn11/21/2022-x3pomo(5:30-7:00),2.addQuestionsToDrive-x2pomo(7:00-8:00),3.(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,4.lruCacheTimed25Min-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.numberOfIslandsTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00)=x11pomo(5:30-11:00)

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)