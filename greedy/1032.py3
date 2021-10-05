n = int(input())

first_sen = list(input())

for i in range(n-1):
	com_sen = list(input())
	for j in range(len(com_sen)):
		if com_sen[j] != first_sen[j]:
			first_sen[j] = '?'

print(''.join(first_sen))


