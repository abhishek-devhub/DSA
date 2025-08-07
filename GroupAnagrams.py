
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]

class Solution():
    def GroupAnagram(self , s:list[str]):
        groups = {}
        for i in s:
            sortedwords = ''.join(sorted(i))
            if sortedwords in groups:
                groups[sortedwords].append(i)
            else:
                groups[sortedwords] = [i]
            print(groups.items())
        return groups.values()
          

anagram = Solution()
print(anagram.GroupAnagram(["act","pots","tops","cat","stop","hat"]))
