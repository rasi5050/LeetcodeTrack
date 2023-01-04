class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
			#creating a placeholder zero at the end; technically mutliplying by 2
            result<<=1        
			
			#setting last bit of binaryNum to 1 if last bit of n is 1, or viceversa; 
			#this can also be written as "result|=(n&1)<<0" because setting the last bit and adding to the last bit is same here
            result+=(n&1)     
			
			#remove the last considered bit from n; technically dividing by 2
            n>>=1       
        return result