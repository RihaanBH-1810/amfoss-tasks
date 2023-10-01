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

