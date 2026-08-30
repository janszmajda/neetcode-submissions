class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, max_l = 0, 0
        window_dict = {} # Stores elements currently in window and their frequencies
        
        for j, value in enumerate(s):
            if value not in window_dict:
                window_dict[value] = 1
            else:
                window_dict[value] += 1
            
            freq_v = max(window_dict, key=window_dict.get)
            # need to get the minority count
            minority_count = 0
            for key,v in window_dict.items():
                if key != freq_v:
                    minority_count += v
            
            # cases based on minority count
            if minority_count <= k:
                max_l = max(max_l, j - i + 1)
            else:
                window_dict[s[i]] -= 1
                i += 1
            
        return max_l

            