#2579 계단오르기

n = int(input())
stairs = []
d = []
for _ in range(n):
  stairs.append(int(input()))

if n == 1:
  print(stairs[0])
elif n ==2:
  print(max(stairs[0]+stairs[1],stairs[1]))
else:
  d.append(stairs[0])
  d.append(max(stairs[0]+stairs[1],stairs[1]))
  d.append(max(stairs[0]+stairs[2],stairs[1]+stairs[2]))

  for i in range(3,n):
    d.append(max(d[i-2]+stairs[i],d[i-3]+stairs[i]+stairs[i-1]))

  print(d.pop())
