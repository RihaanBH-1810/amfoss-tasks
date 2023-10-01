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
