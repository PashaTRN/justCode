class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        Min = min(strs)
        Max = max(strs)
        for i in range(len(Min)):
            if Min[i] == Max[i]:
                result += Min[i]
            else:
                break
        return result
