def b_search(target,array):
  start = 0
  end = len(array) -1 # b의 
  index = -1
  while start <= end:
    mid = (start+end) // 2
    if array[mid] < target:
      index = mid
      start = mid + 1
    else:
      end = mid - 1
  return index



t = int(input())
result = []
for i in range(t):

  a, b = map(int,input().split())
  a_list = list(map(int,input().split()))
  b_list = list(map(int,input().split()))
  a_list.sort()
  b_list.sort()

  cnt = 0

  for i in a_list:
    cnt += b_search(i,b_list) + 1
  
  result.append(cnt)
  #   for j in b_list:
  #     if i>j:
  #       cnt += 1
  #     # if i<j:  1번째 시도
  #     #   break
  # result.append(cnt)


for i in result:
  print(i)
  