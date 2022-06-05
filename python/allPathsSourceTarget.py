class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
<<<<<<< HEAD
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
=======
        
>>>>>>> fe8200d6cec5a8a02df6c22ce7a3d01e21215031
