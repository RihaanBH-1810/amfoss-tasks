t = int(input())
def re_order(n, c):
    flag = True
    count = c
    while flag:
        for i in range(len(n)-1, 0, -1):
            if n[i-1] >= n[i]:
                n[i-1] = n[i-1]//2
                count += 1
        h = sorted(n)
        if h == n:
            if count<10:
                print(count)
            else:
                print(count+1)
            flag = False
while t:
    k = int(input())
    n = list(map(int, input().split()))
    count = 0
    if len(n) == 1:
        count = 0
        print(count)
    elif sorted(n, reverse=True) == n:
        count = -1
        print(count)
    else:
        re_order(n, count)
        
    
    t -= 1
