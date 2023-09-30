def find_min(S):
    c = 0
    while True:
        if c in S:
            c += 1
        else:
            return c
t = int(input())
for _ in range(t):
    s1=[]
    s2=[]
    n = input()
    l = list(map(int, input().split()))

    while l:
        m= max(l)
        for i in range(m+1):
            if i in l:
                count = l.count(i)
                if count == 1:
                    s1.append(i)
                    l.remove(i)
                elif count == 2:
                    s1.append(i)
                    s2.append(i)
                    l.remove(i)
                    l.remove(i)
                elif count > 2:
                    s1.append(i)
                    l.remove(i)
                    while i in l:
                        s2.append(i)
                        l.remove(i)
                else:
                    pass
            else:
                while i in l:
                    s2.append(i)
                    l.remove(i)

    print(find_min(s1)+find_min(s2))
