import inflect

# 🔥 Inflect object create karna
p = inflect.engine()

# 🔢 User se input lo
num = int(input("Enter a number: "))

# 🔡 Number ko words me convert karna
word = p.number_to_words(num).replace(",", "").title() # Title case me karna taake formatting sahi ho

print(f"Output: {word}")