from math import sqrt
counter = 0
number = 2
while counter < 100:
  isPrime = True
  for i in range(2, int(sqrt(number))+1):
    if number%i == 0:
      isPrime = False
      break
    if isPrime:
      counter += 1
      print(number)
    number += 1
