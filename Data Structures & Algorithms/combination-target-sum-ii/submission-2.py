class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index: int, path: List[int]):
            #base case
            s = sum(path)
            if s == target: 
                result.append(path[:])
                return
            
            for i in range (index, len(candidates)):
                if (s + candidates[i]) > target:
                    return
                if i > index:
                    if (candidates[i] == candidates[i-1]):
                        continue
                path.append(candidates[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return result