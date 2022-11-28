class Node:
    def __init__(self,key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.map={}
        self.capacity=capacity
        self.tail, self.head=Node(0, 0), Node(0, 0)
        #tail --> lru, head --> recent
        self.tail.next, self.head.prev=self.head, self.tail      
    
    def insert(self, node):
        prev=self.head.prev
        next=self.head
        node.prev=prev
        node.next=next
        prev.next=node
        self.head.prev=node
        
    def remove(self, node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    def get(self, key: int) -> int:
        if key in self.map: 
            self.remove(self.map[key])
            node = Node(key, self.map[key].val)
            self.insert(node)
            self.map[key]=node
            return self.map[key].val    
        else: return -1

    def put(self, key: int, value: int) -> None:
        node=Node(key, value)
        if key in self.map:
            self.remove(self.map[key])
            self.insert(node)
            self.map[key]=node
        else:
            self.insert(node)
            self.map[key]=node
        if len(self.map)>self.capacity:
            key=self.tail.next.key
            self.remove(self.tail.next)
            del self.map[key]
    #ref: self try3
    #ref:11/28/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day51/52:1.repeat;pairOfSongsDivBy60Timed25Mins-x1pomo(5:30-6:00),2.repeat;minimumAbsoluteDifferenceTimed25Mins-x1pomo(6:00-6:30),3.repeat;lruCacheTimed25Mins-x1pomo(6:30-7:00),4.paypalOa-x2pomo(7:00-8:00),5.addQuestionToDrive,markInInternshipSheet-x2pomo(8:00-9:00)=x7pomo(5:30-9:00)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)