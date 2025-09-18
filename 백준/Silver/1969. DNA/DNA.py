# 1969번
N, M = map(int, input().split()) # N = DNA의 수, M = 문자열의 길이
sum = 0
dna = []
result = []

for n in range(N):
  i = list(input())
  dna.append(i)

for y in range(M):
  lis = [0, 0, 0, 0] # A, C, G, T

  for x in range(N):
    d = dna[x][y]
    if d == 'A' : lis[0] += 1
    elif d == 'C' : lis[1] += 1
    elif d == 'G' : lis[2] += 1
    elif d == 'T' : lis[3] += 1

  sum += N - max(lis)

  i = lis.index(max(lis))
  if i == 0 : result.append('A')
  elif i == 1 : result.append('C')
  elif i == 2 : result.append('G')
  elif i == 3 : result.append('T')

print(''.join(result))
print(sum)