n=int(input())
def rec(n):
    if n%2==0:
        d=n//2
        rec(d)
        print(d)
    else:
        print(n)
rec(n)        
        
