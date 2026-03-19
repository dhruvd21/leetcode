class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # making our adjacent list
        vis = [0]*(n+1)
        adj = [[] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i!= j:
                    adj[i+1].append(j+1)
        
        # dfs
        def dfs(node):
            vis[node] = 1
            for i in adj[node]:
                if vis[i] == 0:
                    dfs(i)
                    

        # iterating dfs through all the graph nodes
        count = 0
        for i in range(1,n+1):
            if vis[i] == 0:
                dfs(i)
                count+=1
        return count