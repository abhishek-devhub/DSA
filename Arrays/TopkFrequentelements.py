class Solution():
    def Frequentelements(self , num:list[int],k:int):
        freq={}
        for i in num:
            if i in freq:
                freq[i] +=1
            else:
                freq[i]=1 
        # SORTING THE VALUES
        sorted_values = sorted(freq.items() , key = lambda x:x[1],reverse=True)
        result=[]
        for j in range(k):
            result.append(sorted_values[j][0])
        return result
Frequent = Solution()
print(Frequent.Frequentelements(num= [1,1,2,2,3,3,3],k=3))
