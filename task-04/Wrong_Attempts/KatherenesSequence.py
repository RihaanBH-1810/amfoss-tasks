n = int(input())
r =[]
first_elements = []
count = 0
def read_input(sol_list):
    global count
    first_elements.append(sol_list[0]) 
    if count:
        if first_elements[count-1] == first_elements[count]:
            r.insert(0, first_elements[count])
            sol_list.pop(0)
    for num in sol_list:
        r.append(num)
    count += 1
        
while n:
    r = []
    first_elements = [] 
    t = int(input())
    count = 0
    for i in range(0,t):
        s = list(map(int, input().split()))
        read_input(s)
    res = []
    [res.append(x) for x in r if x not in res]
    
    print(*res)
    n -= 1
