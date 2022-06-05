class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = triangle[-1]
        print(res)
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
                print(res[j])
        return res[0]

def main():
    s = Solution()
    s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

if __name__ == "__main__":
    main()