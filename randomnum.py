import random
num = random.randint(1,10)
for i in range(3):
    print("Enter your number:")
    a = int(input())
    if a == num:
        print("You won")
    else:
        print("you have", 2-i, "left")
else:
    print("better luck next time")