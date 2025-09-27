# 2644번
# DFS
def dfs(v, num):
  num += 1
  visited[v] = 1
  
  if v == y:
    result.append(num)
  
  for x in graph[v]:
    if visited[x] == 0:
      dfs(x, num)

N = int(input()) # 전체 사람 수
x, y = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
M = int(input()) # 관계의 수

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = []

for m in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(x, 0)

if visited[y] == 0:
  print(-1)
else:
  print(result[0]-1)