import random

x = random.randint(1,6)

while True:
  guess = int(input("enter a number"))
  if guess == x:
    break
  print("guess again!!")
  
print("x = ", x)
print("your guess was true")
