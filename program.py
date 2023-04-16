#Create a program that finds the two-digit positive integer that becomes 7 times smaller when its left-most digit is removed.

for x in range (10, 100):
    z = int(x % 10)
    if x / 7 == z:
        print(x)


