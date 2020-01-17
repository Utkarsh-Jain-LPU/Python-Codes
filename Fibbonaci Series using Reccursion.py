fib={0:0,1:1}
def fibo(n):
    if n in fib:
        return fib[n]
    else:
        fib[n]=fibo(n-1)+fibo(n-2)
        return (fib[n])
a=int(input("Enter Location = "))
print("Element in",a,"location =",fibo(a))    
    
