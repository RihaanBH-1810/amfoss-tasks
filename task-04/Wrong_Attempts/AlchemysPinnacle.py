def adjust_l_r(l_a, l_b):                           
    if len(l_a) > len(l_b):
        l_b = l_b.zfill(len(l_a))
    elif len(l_b) > len(l_a):
        l_b = l_b.zfill(len(l_b))   
    return l_a, l_b
    

t = int(input())

while t:
    L, R = map(int, input().split())
    m_diff = 0
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            Y, J = str(i), str(j)
            if len(Y) != len(J):
                Y, J = adjust_l_r(Y, J)
            diff = 0
            for k in range(len(Y)):
                diff += abs(int(Y[k]) - int(J[k]))
            if diff > m_diff:
                m_diff = diff
    
    print(m_diff)
    t -= 1
