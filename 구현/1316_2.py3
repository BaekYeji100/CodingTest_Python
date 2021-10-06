n = int(input())
count = n

for i in range(n):
	senten = input()
	for j in range(len(senten)-1):
		if senten[j]==senten[j+1]:
			pass
		elif senten[j] in senten[j+1:]:
			count -= 1
			break
	
print(count)
	
			
				