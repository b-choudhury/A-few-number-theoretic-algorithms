#Uses python3
import sys
def calc_pisano_period(m):
    arr1 = []
    arr2 = []
    arr1.append(0)
    arr1.append(1)
    arr2.append(arr1[0]%m)
    arr2.append(arr1[1]%m)
    i=1
    while (arr2[i-1]!=0 or arr2[i]!=1) or i==1:
          arr1.append((arr1[i-1]+arr1[i]))
          arr2.append((arr1[len(arr1)-1])%m)
          i+=1
    return i-1

def F_nmodm(n,m):
    period = calc_pisano_period(m)
    n_ = n%period
    if n_<n:
       arr = []
       arr.append(0)
       arr.append(1)
       if n_==0:
          return arr[0]
       if n_==1:
          return arr[1]
       else:
          for i in range(2,n_+1):
              arr.append(arr[i-1]+arr[i-2])
       return (arr[n_]%m)
    else:
       arr = []
       arr.append(0)
       arr.append(1)
       if n==0:
          return arr[0]
       if n==1:
          return arr[1]
       else:
          for i in range(2,n+1):
              arr.append(arr[i-1]+arr[i-2])
       return (arr[n]%m)


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(F_nmodm(n,m))
