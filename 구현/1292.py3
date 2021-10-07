a, b = map(int,input().split())
result = []

for i in range(b+1): # 
	for j in range(i):
		if len(result) == b:
			break
		result.append(i)

print(sum(result[a-1:b]))


