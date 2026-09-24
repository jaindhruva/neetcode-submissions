class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long_pref = strs[0]

        for i in range (1, len(strs)):
            str2 = strs[i]
            for j in range(0, len(long_pref)):
                if j>=len(str2) or long_pref[j] != str2[j]:
                    long_pref = long_pref[0:j]
                    break
                if long_pref[j] == str2[j]:
                    continue
        
        return long_pref
        