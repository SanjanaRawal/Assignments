def factorail(n) :
    if n<2 :
        return 1
    else :
        return n * factorail(n-1)

num = int(input("Enter a number : "))
if num>=0 :
    ans = factorail(num)
    print(ans)
else :
    print("Factorials of negative numbers doesn't exist")