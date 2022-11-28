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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)