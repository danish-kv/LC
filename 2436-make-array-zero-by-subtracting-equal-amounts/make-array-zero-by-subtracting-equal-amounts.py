class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        res = [i for i in set(nums) if i != 0]
        print(res)
        return len(res)