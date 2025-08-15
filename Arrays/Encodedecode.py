class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res

soln = Solution()

# print(soln.decode(soln.encode([])))        this gives me confusion refer when you are free
# print(soln.decode(soln.encode([""])))     
print(soln.decode(soln.encode(["cat",'acr','tommy','abhisek'])))
