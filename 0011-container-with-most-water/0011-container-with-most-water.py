class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        currentarea=(end-start)*min(height[start],height[end])
        max_height=max(height)

        while start<end:
            currentarea=max(currentarea,((end-start)*min(height[start],height[end])))

            if currentarea > max_height*(end-start):
                return currentarea

            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        
        return currentarea