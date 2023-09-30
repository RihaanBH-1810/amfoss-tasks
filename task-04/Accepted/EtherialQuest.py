n = int(input())
total_vector = [0, 0, 0]

for _ in range(n):
    vector = list(map(int, input().split()))
    for i in range(3):
        total_vector[i] += vector[i]

if total_vector == [0, 0, 0]:
    print("YES")
else:
    print("NO")
