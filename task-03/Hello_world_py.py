number = int(input("Enter the number :"))
if number <= 1:
    exit()
print(2)
for n in range(2,number+1):
    for j in range(2,n):
        if(n%j)==0:
            break;
        elif(n%j)!=0:
            print(n)
            break;
