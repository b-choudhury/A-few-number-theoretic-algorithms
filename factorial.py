def factorial(x):
         if x==0:
         res = float(1)
      else:
         res = float(x*factorial(x-1))
      return res
