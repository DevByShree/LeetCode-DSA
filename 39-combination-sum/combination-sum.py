class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, path, remaining):
            # base case
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # choose element
                path.append(candidates[i])
                
                # same index pass karenge (reuse allowed)
                backtrack(i, path, remaining - candidates[i])
                
                # backtrack
                path.pop()
        
        backtrack(0, [], target)
        return result