class pair_elements:
    def twosum(self,nums,target):
        Lookup={}
        for i,num in enumerate(nums):
            if target-num in Lookup:
                return Lookup[target-num],i           
            Lookup [num]=i
value=int(input("enter the sum"))
print("index1 = %d , index2 = %d" %pair_elements().twosum((10,20,30,40,5060,70),value))