from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        i = 0

        for key, val in c.items():
            if i < k:
                heapq.heappush(heap, (val, key))
                i += 1
            else:
                heapq.heappushpop(heap, (val, key))
        
        output = []
        for x, y in heap:
            output.append(y)
        
        return output