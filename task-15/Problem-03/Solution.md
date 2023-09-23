```
def find_largest_prime(arr):
    l_p = 0
    for ftr in arr:
        if isprime(ftr) and ftr > 0:
            l_p = ftr
    print(l_p)
            
def isprime(ftr):
    is_p = True
    if ftr == 1:
        is_p = False
        return is_p
    elif ftr > 1:
        for i in range(2, ftr):
            if (ftr % i) == 0:
                is_p = False
                break
    return is_p
    

    
def get_fac(n):
    fac = []
    for i in range(1, n+1):
        if n%i == 0:
            fac.append(i)
    return fac

t = int(input())
while(t):
    n = int(input())
    f = get_fac(n)
    find_largest_prime(f)
    t -= 1
        
#Again i encountered time limit exceeded on test case 4 and 5         
#Points (60/100)
```
```
cases = int(input())
while cases > 0:
	number = int(input())
	div = 2
	ans = 0
	maxFact = 0
	while number != 0:
	    if number % div != 0:
		div = div + 1
	    else:
		maxFact = number
		number = number // div
		if number == 1:
		    print(maxFact)
		    ans = 1
		    break
cases -= 1
```
# I searched for a different method and came up with a new method, but still this one is failing the 5th test case
#Points(80/100)



