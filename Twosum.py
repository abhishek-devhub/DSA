class Solution:
    def SumIndex(self,nums:list[int],target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                addindex = nums[i]+nums[j]
                if target == addindex and i!=j:
                    return i,j
        return "No soln found"

Twosum = Solution()
print(Twosum.SumIndex([1,2,3,4],3))

# for reference
# nums = [1,2,3,4,5]
# target = 5
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         sum = nums[i]+nums[j]
#         if target == sum:
#             print(sum,i,j)
#     break