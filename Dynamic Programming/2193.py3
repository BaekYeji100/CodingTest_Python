#2193 이친수

n = int(input())

d = []

d.append(0) # 0
d.append(1) # 1
d.append(1) # 2

for i in range(3,91):
  d.append(d[i-1] + d[i-2])

print(d[n])

