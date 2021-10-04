n = int(input())
seat = input()

l = seat.count("LL")
print(min(n+1-l,n))