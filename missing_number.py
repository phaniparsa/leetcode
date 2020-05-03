class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #declare variables to be used
        max_ele = 0
        arr_xor_val = 0
        overall_xor_val = 0

        #for loop to find out the xor value of all elements in the given array, and max element
        for each_num in nums:
            arr_xor_val ^= each_num
            if max_ele < each_num:
                max_ele = each_num
        
        #for loop to find out the xor values from 0 till max_ele
        for j in range(1, max_ele+1):
            overall_xor_val ^= j
        
        #returns the missing value in the input array
        return overall_xor_val^arr_xor_val