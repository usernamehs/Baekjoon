# 2606번
# DFS
def dfs(v):
  visited[v] = 1
  for x in graph[v]:
    if visited[x] == 0: # 아직 방문한적 없는 경우
      dfs(x)

C = int(input())
N = int(input())
graph = [[] for i in range(C+1)]
visited = [0]*(C+1)

for i in range(N):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)

print(sum(visited)-1)