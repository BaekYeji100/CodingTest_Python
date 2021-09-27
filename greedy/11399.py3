human = int(input())

time = list(map(int,input().split()))
time.sort()

per_time = 0
result = 0

for i in time:
    per_time += i
    result += per_time
    
print(result)