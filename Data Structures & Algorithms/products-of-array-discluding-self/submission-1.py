class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with help
        n = len(nums)
        output = [0] * n
        product = 1
        zeroCount = 0
        
        for i in range(n):
            if (nums[i] != 0):
                product = product * nums[i]
            else:
                zeroCount = zeroCount + 1
                
        if (zeroCount == 1):
            for j in range(n):
                if (nums[j] == 0):
                    output[j] = product
                else: 
                    output[j] = 0
        elif (zeroCount == 0):
            for j in range(n):
                output[j] = product // nums[j]
        return output