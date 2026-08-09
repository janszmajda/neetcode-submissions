class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        The numbers list is sorted so can take first element and compare with last. 
        if > goal then need to move right pointer down
        if < than goal need to move left pointer up
        """
        n = 1
        i = 0
        for x in range(len(numbers)):
            # print(numbers[i] + numbers[len(numbers) - n])
            # print(n)
            # print(numbers[len(numbers) - n])
            if numbers[i] + numbers[len(numbers) - n] > target:
                #move right pointer down then retry
                n += 1
            elif numbers[i] + numbers[len(numbers) - n] < target:
                #move left pointer up
                i += 1
            else:
                return [i + 1, len(numbers) - n + 1]