i = 1
while True:
    day =  0
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V==0:
        break
        
    day += (V//P)*L + min((V%P),L)
    print("Case {0}: {1}".format(i,day))
    i += 1

