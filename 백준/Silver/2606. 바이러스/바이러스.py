# 2606번
from collections import deque

C = int(input())
N = int(input())
graph = [[] for i in range(C+1)]
visited = [0]*(C+1)

for i in range(N):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
# print(graph)

visited[1] = 1

# BFS
Q = deque([1])
while Q:
  current = Q.popleft()
  for x in graph[current]:
    if visited[x] == 0: # 아직 방문한적 없는 경우
      Q.append(x)
      visited[x] = 1
    
print(sum(visited)-1)