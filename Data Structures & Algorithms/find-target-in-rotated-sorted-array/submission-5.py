class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        minimum = low

        if target >= nums[minimum] and target <= nums[len(nums) - 1]:
            low = minimum
            high = len(nums) - 1
        else:
            low = 0
            high = minimum - 1
        
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        return -1


        