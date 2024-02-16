from collections import deque
def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g,i,visited):
    queue = deque([i])
    visited[i] = 1
    while queue:
        i = queue.popleft()
        print(chr(ord('A') + i), end=' ')
        for j in range(len(g)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = 1

graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 0, 1, 0, 0],
         [1, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 0]]

visited = [0 for i in range(len(graph))]
dfs(graph, 0, visited)
visited = [0 for i in range(len(graph))]
print()
bfs(graph, 0, visited)