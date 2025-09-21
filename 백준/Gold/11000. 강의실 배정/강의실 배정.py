# 11000번
import sys
import heapq

N = int(input()) # 수업의 개수
lis = []

for n in range(N):
  x = list(map(int, input().split()))
  lis.append(x)

lis.sort()

heap = [lis[0][1]]
for n in range(N-1):
  if heap[0] <= lis[n+1][0]:
    heapq.heappop(heap)
  heapq.heappush(heap, lis[n+1][1])

print(len(heap))