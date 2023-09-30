arr = input()
arr = list(arr)
i = 0
solution = "hello"

for j in arr:
    if j == solution[i]:
        i += 1
    if i == 5: 
        break

if i == 5:
    print("YES")
else:
    print("NO")
