# 11725번
# BFS
from collections import deque

N = int(input()) # 노드의 개수

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = [0]*(N+1)

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited[1] = 1

# BFS
Q = deque([1])
while Q:
  current = Q.popleft()
  for x in graph[current]:
    if visited[x] == 0: # 아직 방문한적 없는 경우
      Q.append(x)
      visited[x] = 1
      result[x] = current

for n in range(2, N+1):
  print(result[n])