class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx, key in enumerate(nums):
            complement = target - key
            if complement in hashMap:
                return [hashMap[complement], idx]

            hashMap[key] = idx

        return 