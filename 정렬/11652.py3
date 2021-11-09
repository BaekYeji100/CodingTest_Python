# 11652 카드
import sys
from collections import Counter

n = int(input())
arr= []
for i in range(n):
	arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
arr_cnt=Counter(arr).most_common(1)
print(arr_cnt[0][0])