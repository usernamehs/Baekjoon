# 10610번
N = list(map(int, input()))
N.sort(reverse=True)

if (sum(N) % 3 == 0) and (N[-1] == 0) : 
  for n in N:
    print(n, end='')

else : 
  print(-1)