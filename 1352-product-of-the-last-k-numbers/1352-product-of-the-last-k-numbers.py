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