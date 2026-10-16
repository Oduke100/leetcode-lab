class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        index = 0
        answer = ""

        for i in range(len(strs)):
            for char in strs[i]:
                for w in strs:
                    if index <= len(w)-1 and all(w[index] == char):
                        answer = answer + char

                        index += 1

        return answer

test = Solution()
answer = test.longestCommonPrefix(["", "bo"])
print(answer)
