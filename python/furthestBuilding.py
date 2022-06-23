from sortedcontainers import SortedDict
class Solution:  
    def furthestBuilding(self, A, bricks, ladders):
        heap = []
        for i in range(len(A) - 1):
            d = A[i + 1] - A[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(A) - 1

def main():
    s = Solution()
    heights = [1,2]
    brick = 0
    ladder = 0
    print(s.furthestBuilding(heights, brick, ladder))

if __name__ == "__main__":
    main()