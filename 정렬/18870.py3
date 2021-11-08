import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr_set = sorted(list(set(arr)))

# print(arr_set)
# 시간초과
# for i in arr:
# 	for j in range(len(arr_set)):
# 		if i==arr_set[j]:
# 			print(j,end=' ')

dic = {arr_set[i] : i for i in range(len(arr_set))}

for i in arr:
	print(dic[i],end=' ')