def is_binary_palindrome(n):
    # 🔢 Step 1: Convert number to binary (bin() function se, aur [2:] se "0b" hatayenge)
    binary_str = bin(n)[2:]

    # 🔄 Step 2: Palindrome check karne ke liye reverse string compare karna
    if binary_str == binary_str[::-1]:  # Reverse check
        return f'Binary: {binary_str}\nOutput: Palindrome ✅'
    else:
        return f'Binary: {binary_str}\nOutput: Not a Palindrome ❌'

# 🔥 User se input lena
num = int(input("Enter a number: "))


# 🔡 Output print karna
print(is_binary_palindrome(num))
