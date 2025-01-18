class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for xs in zip(*strs):
            if len(set(xs)) > 1:
                break

            i += 1

        return strs[0][:i]
