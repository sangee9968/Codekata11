n=int(input())
def rec(n):
    if n%2==0 and n!=2:
        d=n//2
        rec(d)
        print(d)
    elif n==2:
        d=n//2
        print(d)
    else:
        print(n)
#function call        
rec(n)        
