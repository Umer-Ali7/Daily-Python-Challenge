print("----------------Daily Python Challenge Day 3🐍----------------------")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # Square root tak check karna optimized hai
        if n % i == 0:
            return False
        return True
    

# User Input Lena

num = int(input("Enter a number: "))

# Output dena
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")