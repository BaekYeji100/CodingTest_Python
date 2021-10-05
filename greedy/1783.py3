n, m = map(int,input().split())

if n==1:
	move = 1

elif n==2:
	move = min(4,(m+1)//2)
	# 4 인 경우는 m >= 7 
elif m < 7:
	move = min(4,m)

else:
	move = (2+(m-5)) + 1

print(move)
	


	

	