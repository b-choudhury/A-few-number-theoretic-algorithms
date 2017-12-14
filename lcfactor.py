#Uses python3
import sys
def euclid_gcd(a,b):
    if b==0:
       return a
    else:
       a_ = a%b
       return euclid_gcd(b,a_)


def lcfactor(a,b):
    if b==0:
       return a
    else:
       gcd = euclid_gcd(a,b)
       return int((a*b)//gcd)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcfactor(a, b))



