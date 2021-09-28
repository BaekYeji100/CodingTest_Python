t = int(input())
card = []
for _ in range(t):
	n = int(input())
	card.append(list(input().split()))

for i in card:
	result = []
	for j in range(len(i)):
		if j == 0:
			result.append(i[j])
		elif result[0] >= i[j]:
			result.insert(0,i[j])
		else:
			result.append(i[j])

	print("".join(result))
	