# 1. 1+- 2.MHz로 가는 방법
A,B = map(int,input().split())
N = int(input())
MHz = []

for i in range(N):
	MHz.append(int(input()))
	MHz[i] = abs(MHz[i]-B)

want_MHz = abs(A-B)
want_MHz2 = min(MHz)

print(min(want_MHz,want_MHz2+1)) 