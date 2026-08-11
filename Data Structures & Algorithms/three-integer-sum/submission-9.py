class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        #goal: use two pointer approach while iterating through the 3rd thing
        numl = sorted(nums)
        for i in range(len(numl)):
            if numl[i] == numl[i-1] and i > 0:
                continue
            else:
                f = i + 1
                l = len(numl) - 1
                while f < l:
                    if numl[f] + numl[l] + numl[i] > 0:
                        l -= 1
                    elif numl[f] + numl[l] + numl[i] < 0:
                        f += 1
                    else:
                        temp = [numl[f], numl[i], numl[l]]
                        if temp not in ans:
                            ans.append(temp)
                        f += 1
                        l -= 1
        return ans