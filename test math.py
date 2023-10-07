import math

"""def rotated(a):
  m = len(a[0])
  n = len(a) 

  result = [[0]* n for k in range(m)] 

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result """

def anti_clock_rotated(a):
  m = len(a[0])
  n = len(a) 

  result = [[0]* n for k in range(m)] 

  for i in range(n):
    for j in range(m):
      result[m-j-1][i] = a[i][j]
  return result

arr=[[' ']* 80 for k in range(42)]  
        
for k in range(42):
    degree=k*9
    second_chg=int(math.sin(math.radians(degree))*40+40)        
    for p in range(second_chg):
        arr[k][p]='#'

for i in anti_clock_rotated(arr):
    for j in i:
        print(j,end=' ')
    print()