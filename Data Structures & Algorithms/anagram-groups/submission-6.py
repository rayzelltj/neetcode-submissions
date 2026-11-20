class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # *had some helpp
        #got the logic and dictionary method, just needed syntax help
        #also tuple help sorted() returns a list -> can't be a key by itself

        seen = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if (key not in seen):
                seen[key] = []
            seen[key].append(strs[i])
        # output = []
        # for num_list in seen.values():
        #     output.append(num_list)
        # return output
        return list(seen.values())

        #The time is O(n · k log k): you loop over n words, and each one gets sorted, which costs k log k. The space is O(n · k)