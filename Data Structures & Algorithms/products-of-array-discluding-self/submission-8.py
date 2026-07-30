class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1 for x in range(len(nums))] # [1,1,...]

        #want array of all the other elements multiplied in that given position
        for i in range(len(nums)):
            mult = 1
            for x in range(len(nums)):
                if x != i:
                    mult *= nums[x]
            answers[i] = mult
        return answers