# 2678번
count = 0 # 빙고 개수
result = 0 # 순서
cross1 = 0 # 대각선 [0][0], [1][1], [2][2], [3][3], [4][4]
cross2 = 0 # 대각선 [0][4], [1][3], [2][2], [3][1], [4][0]

bingo = []
for i in range(5):
  x = list(map(int, input().split()))
  bingo.append(x)

answer = []
for i in range(5):
  x = list(map(int, input().split()))
  answer.append(x)



for x in range(5):
  for y in range(5):
    f = answer[x][y]
      
    for z in range(5):
      if count >= 3 : break
      if f in bingo[z]:
        ty = bingo[z].index(f)
        bingo[z][ty] = 0
        result += 1

        if (z == 0 and ty == 0) or (z == 1 and ty == 1) or (z == 2 and ty == 2) or (z == 3 and ty == 3) or (z == 4 and ty == 4):
          cross1 += 1
          if cross1 == 5: count += 1

        if (z == 0 and ty == 4) or (z == 1 and ty == 3) or (z == 2 and ty == 2) or (z == 3 and ty == 1) or (z == 4 and ty == 0):
          cross2 += 1
          if cross2 == 5: count +=1

        if (len(set(bingo[z])) == 1):
          count += 1

        if (bingo[0][ty] == 0 and bingo[1][ty] == 0 and bingo[2][ty] == 0 and bingo[3][ty] == 0 and bingo [4][ty] == 0):
          count += 1

print(result)