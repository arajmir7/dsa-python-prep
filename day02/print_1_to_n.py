def printnumbers(current, n):
    if current > n:
        return
    print(current, end=" ")
    printnumbers(current+1, n)
n=10
printnumbers(1,n)