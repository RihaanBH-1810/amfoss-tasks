#My 1st approach for this problem :

t = int(input())

while(t):
    n = int(input())
    count = 0 
    for i in range(1,n):
        if (i%3 == 0) or (i%5 == 0):
            count += i
    print(count) 
    t -= 1
    
But this just scored 60 points and it showed time limit exceeded on two test cases

#My 2nd approach for this problem :
#After a few googling i tried to solve it through arithmetic progression
#It still gave time limit exceeded on two test cases and scored only 60

t = int(input())
sum = 0
def som(k,n):
    y = (n-1)//k
    sum =  y*(2*k + (y-1)*k)/2
    return int(sum)
while(t):
    n = int(input())
    count = som(3,n)+som(5,n)-som(15,n)
    print(count)
    t -= 1


#Then i found a solution on google , This is not my solution but i read it and i understood it , and this time it worked and scored 100

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



