import random  # 🔹 Random number generate karne ke liye module import

def number_guessing_game():
    """🎯 Number Guessing Game"""

    # 🔢 Step 1: 1-100 ke beech ek random number generate karo
    secret_number = random.randint(1,100)

    print("\n🎮 WELCOME TO THE NUMNER GUESSING GAME!")
    print("🔢 Guess the number (between 1 and 100)")


    while True: # 🔄 Infinite loop (Jab tak sahi guess na ho)
        try:
            # 🎯 Step 2: User ka input lena (integer me convert karna zaroori hai)
            guess = int(input("Enter your guess: "))

            # ✅ Step 3: Check if guess is correct
            if guess == secret_number:
                print(f"🎉 Congratulation! You guessed it right {secret_number}! 🎯")
                break  # 🔥 Loop exit karna kyunki sahi guess ho gaya

            # 🔼 Step 4: Agar guess chhota ho to user ko batao
            elif guess < secret_number:
                print("📉 Too low! Try again.")

            # 🔽 Step 5: Agar guess bada ho to user ko batao
            else:
                print("📈 Too high! Try agian.")

        except ValueError:
            # ⚠️ Agar user ne invalid input diya (e.g., string), to error handle karo
            print("⚠️ Please enter a valid number!")


# 🔥 Game start karo
if __name__ == "__main__":
    number_guessing_game()