import re  # 🔹 Regular Expressions ka use karne ke liye module import

def check_password_strength(password):
    """🔐 Password Strength Checker"""

    # ✅ Step 1: Password length check karo
    if len(password) < 6:
        return "❌ weak (Password should be at least 6 characters long!)"
    
    # 🔹 Step 2: Different conditions check karne ke liye flags set karo
    has_upper = bool(re.search(r"[A-Z]", password))  # 🔼 Uppercase letter check
    has_lower = bool(re.search(r"[a-z]", password))  # 🔽 Lowercase letter check
    has_digits = bool(re.search(r"\d", password))    # 🔢 Number check
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)) # 🔥 Special character check

    # ✅ Step 3: Password ko categorize karo
    if not (has_upper or has_digits or has_special):
        return "❌ weak (Use a mix of letters, numbers, and symbols!)"

    if len(password) >= 8 and (has_upper or has_digits):
        if has_special:
            return "✅ Strong (Good job! Your password is secure.)"
        return "⚠ Moderate (Add special characters to make it stronger!)"
    return "❌ weak (Try adding more variety to your password!)"

# 🔥 User se password input lo
if __name__ == "__main__":
    user_password = input("🔐 Enter your password: ")
    strenght = check_password_strength(user_password)
    print(f"🔍 Password Strenght: {strenght}")