# 2178
from collections import deque

# BFS
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  result = 0
  Q = deque()
  Q.append((x, y))

  while Q:
    x, y = Q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        Q.append((nx,ny))
      
  return graph[N-1][M-1]


N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
# visited = [[0]*(M) for _ in range(N)]

print(bfs(0,0))