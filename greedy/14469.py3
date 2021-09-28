n = int(input())
cow = []
time = 0
for i in range(n):
	cow.append(list(map(int,input().split())))

cow.sort()

for a_t,t_t in cow:
	if time < a_t:
		time = a_t
	time += t_t

print(time)


			   