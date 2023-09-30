a = "amfoss          "
n = int(input())

while(n):
    s = input()
    if len(s)>=10:
        exit()
    counter = 0
    for i in range(0,len(s)):
        if(s[i] != a[i]):
            counter += 1
    print(counter)
    n -= 1

