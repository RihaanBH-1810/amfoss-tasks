```
def find_sum(N):
    f1 = 1
    f2 = 1
    ev_sum = 0
    while True:
        f = f2 + f1 
        if f >= N: 
            return ev_sum
        if f % 2 == 0:
            ev_sum += f
        f1 = f2
        f2 = f
        
t = int(input())
while t:
    N = int(input())
    print(find_sum(N))
    t -= 1
```
#This problem was comparatively easy as i did not encounter any time limit exceeded error 

