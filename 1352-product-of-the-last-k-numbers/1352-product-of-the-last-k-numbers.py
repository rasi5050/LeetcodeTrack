class ProductOfNumbers:
    #do naive algorithm
    """working code; commented for alter    
    def __init__(self):
        self.stream=[]
        self.prefixProd=[]
    #do as prefix prod
    def add(self, num: int) -> None:
        if self.stream:
            self.prefixProd.append(self.prefixProd[-1]*num)
        else:
            self.prefixProd.append(num)
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        # print(self.stream, self.prefixProd, k)
        if k==len(self.stream):
            return self.prefixProd[-1]
        elif self.prefixProd[-1]==0 and self.prefixProd[-(k+1)]!=0: #zero is within the last k
                return 0
            
        elif self.prefixProd[-1]==0 and self.prefixProd[-(k+1)]==0: #zero can from somewhere else; hence need to calculate actual product
            return(prod(self.stream[len(self.stream)-k:]))
        return self.prefixProd[-1]//self.prefixProd[-(k+1)]   #if values other than zeroes
            
        """
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
    def __init__(self):
        self.prefixProd=[1]     #1 is the multiplicative identity
    #do as prefix prod
    def add(self, num: int) -> None:
        if num==0:
            self.prefixProd=[1]
        else:
            self.prefixProd.append(self.prefixProd[-1]*num)

    def getProduct(self, k: int) -> int:
        if k>=len(self.prefixProd): return 0
        return self.prefixProd[-1]//self.prefixProd[-(k+1)]
    
    #status: succes; help(https://leetcode.com/problems/product-of-the-last-k-numbers/discuss/510260/JavaC%2B%2BPython-Prefix-Product)
    #Analysis: Time O(1), Space O(n)
    #ref: 1/27/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day94/94Blind30/75,2q/dayDay13/12;doLeetcode3Question/Day:1.P1:1.numberOfGoodLeafNodesPairsTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.productOnLastKNumbersTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.binaryTreeLevelOrderTraversalTimed25Mins-x1pomo(8:00-8:30),6.cloneGraph-x1pomo(8:30-9:00),7.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.courseSchedule-x1pomo(10:00-10:30)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)early(6:00-10:30)
