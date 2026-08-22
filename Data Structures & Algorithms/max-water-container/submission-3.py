class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer solution
        max_area = 0 #min(heights[0], heights[len(heights) - 1]) * (len(heights) - 1)
        i, j = 0, len(heights) - 1

        while True:
            if i == j:
                break
            h_i, h_j = heights[i], heights[j]
            area = min(h_i, h_j) * (j - i)
            
            if area < max_area and h_i < h_j:
                i += 1
            elif area < max_area and h_i >= h_j:
                j -= 1
            else:
                max_area = area
                if h_i <= h_j:
                    i += 1
                else:
                    j -= 1
            
        return max_area