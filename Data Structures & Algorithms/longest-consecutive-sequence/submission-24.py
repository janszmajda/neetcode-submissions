class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #can only do with one for loop
        #want sequence of numbers that are 1 away from each other

        no_dupes = sorted(set(nums)) #--> [1,2,3,...]

        
        #do it without counting
        all_counts = []
        current = []
        for i in range(len(no_dupes)):
            if len(current) == 0 or abs(no_dupes[i] - no_dupes[i-1]) == 1:
                current.append(no_dupes[i])
            else:
                all_counts.append(current)
                current = []
                current.append(no_dupes[i])
        all_counts.append(current)
        print(all_counts)

        max_len = max(len(elem) for elem in all_counts)
        return max_len