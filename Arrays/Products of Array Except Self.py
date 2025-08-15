class Solution():
    def productofarrays(self , num:list[int]):
        arr =[]
        for i in range(len(num)):
            mul = 1
            for j in range(len(num)):
                if(i!=j):
                    mul *= num[j]
            arr.append(mul)
        return arr
                    
soln = Solution()
print(soln.productofarrays([1,2,3,4]))