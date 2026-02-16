def printnumbers(current, n):
    if current > n:
        return
    
    printnumbers(current + 1, n)
    print(current, end=" ")
    

n=5
printnumbers(1, n)