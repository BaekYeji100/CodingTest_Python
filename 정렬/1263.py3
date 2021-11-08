n = int(input())
arr= []
for i in range(n):
	t,s = map(int,input().split())
	arr.append((s,t))

arr.sort(reverse=True)

for i in range(n):
	if i == 0:
		dif = arr[i][0] - arr[i][1]
		continue
	else:
		if dif <= arr[i][0]:
			dif = dif -arr[i][1]
		else:
			dif = arr[i][0] - arr[i][1]
			
if dif >= 0:
	print(dif)
else:
	print(-1)
