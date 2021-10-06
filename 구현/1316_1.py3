n = int(input())
count = 0

for i in range(n):
	senten = list(input())
	alpha=[]
	for j in range(len(senten)):
		if j != len(senten)-1:
			if senten[j]==senten[j+1]:
				pass
			elif senten[j]!=senten[j+1]:
				if senten[j] in alpha:
					break
				alpha.append(senten[j])
		else:
			if senten[j] in alpha:
				break
			count+=1

print(count)
	
			
				