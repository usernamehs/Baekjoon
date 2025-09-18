# 11047번
N, K = map(int, input().split()) # N = 동전의 종류, K = 가치의 합

min = 0 # 최솟값
change = K
coin = [] # 동전의 가치

for n in range(N) :
  x = int(input())
  coin.append(x)

for n in range(N - 1, -1, -1):
  min += change // coin[n]
  change %= coin[n]

print(min)