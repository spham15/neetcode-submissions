class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefixSum = 1

        for i in range(len(nums)):
            res[i] = prefixSum
            prefixSum *= nums[i]
                
        postfixSum = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfixSum
            postfixSum *= nums[j]

        return res
