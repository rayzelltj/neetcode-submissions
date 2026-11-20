class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if (key not in seen):
                seen[key] = []
            seen[key].append(strs[i])
        output = []
        for num_list in seen.values():
            output.append(num_list)
        return output