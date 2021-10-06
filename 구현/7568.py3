import sys

n = int(sys.stdin.readline())
kgncm = []
result = []

for i in range(n):
	kg,cm = map(int,sys.stdin.readline().split())
	kgncm.append((kg,cm))

for i in range(n):
	grade = 1
	for j in range(n):
		if kgncm[i][0] < kgncm[j][0] and kgncm[i][1] < kgncm[j][1]:
			grade +=1

	result.append(str(grade))
	
print(" ".join(result))	
