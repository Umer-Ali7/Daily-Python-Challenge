# 📝 To-Do List ko store karne ke liye ek empty list
tasks = []

def add_task():
    """🔹 User se task le kar list me add karega"""
    task = input("Enter new task: ")
    tasks.append(task) # Task list me add ho jayega
    print(f"✅ Task Added! {task}")

def show_tasks():
    """🔹 Saare tasks ko show karega"""
    if not tasks:
        print("📌 No tasks available!")
    else:
        print("\n📋 Your To-Do List:")
        for index, task in enumerate(tasks, start=1): # Index ke sath print karega
            print(f"{index}. {task}")

def delete_task():
    """🔹 Task delete karne ka option"""
    show_tasks()  # Pehle list dikha do
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):   # Valid range check
                remove_task = tasks.pop(task_num - 1)  # Task delete karega
                print(f"❌ Task Removed: {remove_task}")
            else:
                print("⚠ Invalid Task Number!")
        except ValueError:
            print("❌ Please enter a valid number!")


def main():
    """🔹 Main function jo menu show karega aur user ka input lega"""
    while True:
        print("\n📌 Welcome to To-Do List!")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("\nEnter Choice: ")   # User ka input lena
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Exiting... Have a productive day! 🚀")
            break # Loop exit karega
        else:
            print("⚠ Invalid choice! Please enter 1-4.")

# 🔥 Program Start Karein
if __name__ == "__main__":
    main()

