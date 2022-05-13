class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        output = [[0] * c for i in range(r)]
        count = 0
        if r * c != len(mat) * len(mat[0]):
            return mat
        for i in range(r):
            for j in range(c):
                output[i][j] = mat[int(count / len(mat[0]))][count % len(mat[0])]
                count += 1
        return output

def main():
    mat = [[1,2],[3,4]]
    r = 4
    c = 1
    output = [[0] * c for i in range(r)]
    count = 0
    if r * c != len(mat) * len(mat[0]):
        return mat
    for i in range(r):
        for j in range(c):
            output[i][j] = mat[int(count / len(mat[0]))][count % len(mat[0])]
            print(output)
            count += 1
    print(output)



if __name__ == "__main__":
    main()