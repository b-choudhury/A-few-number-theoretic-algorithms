#Uses python3
import sys 

def euclid_gcd(a,b):
    if b==0:
       return a
    else:
       a_ = a%b
       return euclid_gcd(b,a_)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(euclid_gcd(a, b))




