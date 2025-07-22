def knapsack(n, k, w, v, memo):
  if n == 0 or k == 0:
    return 0

  if (n, k) in memo:
    return memo[(n, k)]
  
  if w[n - 1] > k:
    result = knapsack(n - 1, k, w, v, memo)
  else : 
    result = max(
        knapsack(n - 1, k, w, v, memo),
        knapsack(n - 1, k - w[n - 1], w, v, memo) + v[n - 1]
    )

  memo[(n, k)] = result
  return result


memo = {}
w_lis = []
v_lis = []
n, k = map(int, input().split())

for i in range(n):
  w, v = map(int, input().split())
  w_lis.append(w)
  v_lis.append(v)


result = knapsack(n, k, w_lis, v_lis, memo)
print(result)