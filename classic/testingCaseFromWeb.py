

num = 29

print([num % i != 0 for i in range(2, num)])
if all(num % i != 0 for i in range(2, num)):
    print(num, "is a prime")
else:
    print(num, "is not a prime")