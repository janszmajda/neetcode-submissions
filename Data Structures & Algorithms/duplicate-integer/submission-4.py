class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # keep track of numbers seen. goal to iterate through list only once
        L = []
        for elem in nums:
            if elem in L:
                return True
            L.append(elem)
        return False
