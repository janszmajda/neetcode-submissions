class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        for elem in nums:
            goal = target - elem
            if goal in nums[index + 1:len(nums)]:
                if nums.count(goal) > 1:
                    nums.remove(goal)
                    goal_index = nums.index(goal) + 1
                else: 
                    goal_index = nums.index(goal)
                return [index, goal_index]
            index += 1