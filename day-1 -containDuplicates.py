class Solution:
    def containsDuplicate(self,nums):
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False

Duplicates = Solution()
print(Duplicates.containsDuplicate([1,2,3,4,5,1]))