class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_value = 0
        for each_num in nums:
            xor_value ^= each_num
        return 