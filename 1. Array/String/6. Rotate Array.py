class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[:][::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
