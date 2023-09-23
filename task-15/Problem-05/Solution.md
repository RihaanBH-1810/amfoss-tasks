def lcm(a, b):
    lcm = 1
    for i in range(max(a, b), 1 + (a * b)):
        if i % a == i % b == 0:
            lcm = i
            break
    return lcm

def SM(N):
    result = 1
    for i in range(1, N + 1):
        result = lcm(result, i)
    return result

t = int(input())
while t:
    N = int(input())
    result = SM(N)
    print(result)
    t -= 1
    
#I used GPT to get the method and then learnt how to find lcm and implemented the algorithm for finding the smallest number which is divisible by numbers from 1 to N
#Although i understood it later 
 
