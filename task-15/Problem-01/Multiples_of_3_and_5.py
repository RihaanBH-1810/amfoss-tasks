t = int(input())
sum = 0
def som(k,n):
    y = (n-1)//k
    return k * (y * (y + 1)) // 2
    #return int(sum)
while(t):
    n = int(input())
    count = som(3,n)+som(5,n)-som(15,n)
    print(count)
    t -= 1


