import random
k = random.randrange(1,10)
guess = int(input("Enter any number: "))
while k!= guess:
    if guess < k:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > k:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")