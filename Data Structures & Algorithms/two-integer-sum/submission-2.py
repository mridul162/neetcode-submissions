class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff={}

        for i, n in enumerate(nums):
            numDiff = target - n;
            if numDiff in diff:
                return [diff[numDiff], i]
            diff[n] = i
        