#Uses python3

def last_dig_fib(n):
    arr = []
    arr.append(0)
    arr.append(1)
    if n==0:
       return arr[0]
    if n==1:
       return arr[1]
    else:
       for i in range(2,n+1):
           arr.append((arr[i-1]+arr[i-2])%10)
       return arr[n]


n = int(input())
print(last_dig_fib(n))
