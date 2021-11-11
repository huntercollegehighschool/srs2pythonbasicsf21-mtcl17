"""
Define a function sumofsquares that takes an integer input number. The function then adds all the first n perfect squares (starting from 1).

For example, sumofsquares(3) should return 14, since 1 + 4 + 9 = 14.
"""

def sumofsquares(number):
  i=1
  sumsquares=0
  while i<=number:
    sumsquares+=i**2
    i+=1
  return sumsquares