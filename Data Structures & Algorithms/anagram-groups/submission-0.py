class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            if (tuple(sorted(strs[i])) in seen):
                seen[tuple(sorted(strs[i]))].append(strs[i])
            else:
                seen[tuple(sorted(strs[i]))] = []
                seen[tuple(sorted(strs[i]))].append(strs[i])
        output = []
        for num_list in seen.values():
            output.append(num_list)
        return output