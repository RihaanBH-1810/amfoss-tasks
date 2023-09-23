#This one is also failing just one test case
#(80/100)
```
def palc(n):
    near = n - (n % 11)
    for i in range(near, 100001, -11):
        if str(i) == str(i)[::-1]:
            j = 990
            while j >= 110:
                if i % j == 0 and len(str(i // j)) == 3:
                    return i
                j -= 11

t = int(input())
while t:
    N  = int(input())
    print(palc(N))
    t -= 1
```
