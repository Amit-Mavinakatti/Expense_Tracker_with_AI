from openai import OpenAI

def start_ai_chat(client, expenses_list, budget_list, income):
    """Start infinite AI chat with financial awareness"""
    print("\n==========================================================: AI Mode :================================================================")
    print("🤖 AI is ready! You can ask finance-related questions, savings tips, or general advice.")
    print("Type 'quit' to exit AI mode.\n")

    
    expense_summary = "\n".join([f"{a}: Rs.{b}" for a, b in zip(expenses_list, budget_list)])
    context = f"""
    I am tracking my monthly expenses.
    Monthly Income: Rs.{income}
    My Expenses and Budgets:
    {expense_summary}

    Use this data whenever needed to provide personalized financial advice.
    """

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nExiting AI Mode... Thank You!")
            break

        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=context + "\nUser Question: " + user_input
            )
            print("\nAI:", response.output_text, "\n")
        except Exception as e:
            print("⚠ AI Error:", str(e))


print("\n\n=========================================: Smart Expense Tracker with AI :========================================\n")
print("Hey Welcome!")
print("Here's our smart tool Expense Tracker with AI. Manage and analyze your expenses intelligently!")
print("Let's GO....\n")

try:
    # User info
    name = input("User Name: ")
    Email = input("Email    : ")
    password = input("Password : ")

    while True:
        try:
            income = int(input("\nEnter Your Monthly Earnings (in Rs.): "))
            break
        except ValueError:
            print("❌ Please enter a valid number for income. Try again!")

    secured = "#####" + str(password[-1]) if password else "#####"

    print("\n====================================================:Expense Tracker:==========================================\n")
    print("Account Details:\n")
    print("USER NAME :", name.upper())
    print("Email     :", Email.upper())
    print("Password  :", secured)
    print("TOTAL INCOME : ", income)

    expenses_list = []
    budget_list = []

    print("\n=========================================: Main Menu :=====================================")
    print("1) Start Tracking Expenses")
    print("2) Exit")
    option = input("\nEnter Your option: ")

    if option == '1':
        print("\nDo you want to add new expenses? (y/n)")
        option2 = input("Enter Here: ")

        if option2.lower() == 'y':
            while True:
                try:
                    num = int(input("How many expenses do you want to add? : "))
                    break
                except ValueError:
                    print("❌ Please enter a valid number!")

            print("\nEnter " + str(num) + " Expenses\n")
            for i in range(num):
                expense = input(f"Expense {i+1}: ")
                expenses_list.append(expense)

            print("\nDo you want to add budget for your expenses? (y/n)")
            option3 = input("Enter: ")

            if option3.lower() == 'y':
                for i in range(len(expenses_list)):
                    while True:
                        try:
                            print(f"Add budget for {expenses_list[i]} (in Rs.):")
                            budget = int(input("Your Budget: "))
                            budget_list.append(budget)
                            break
                        except ValueError:
                            print("❌ Please enter a valid number for budget.")

            print("\n=============== Expense Summary ==========================\n")
            print("Expenses" + "   " + "Budget(in Rs.)\n")
            for a, b in zip(expenses_list, budget_list):
                print(f"{a} = Rs.{b}")

            print("\nYour Total Expenses: ", len(expenses_list))
            print("Your Total Income : Rs.", income)
            print("Your Total Budget : Rs.", sum(budget_list))

            if budget_list:
                print("Highest Budget : Rs.", max(budget_list))
                print("Lowest Budget  : Rs.", min(budget_list))

            if income > sum(budget_list):
                print("\n✅ Your expenses are under control. Keep it up!")
            else:
                print("\n⚠ Warning: Your expenses exceed your income! Try to reduce spending.")

            # ===== AI INTEGRATION =====
            use_ai = input("\nDo you want AI to analyze and assist you? (y/n): ")
            if use_ai.lower() == 'y':
                try:
                    client = OpenAI(api_key="")  # Replace with your key
                    start_ai_chat(client, expenses_list, budget_list, income)
                except Exception as e:
                    print("⚠ Could not start AI Analysis:", str(e))
        else:
            print("\nNo expenses added. Exiting...")

    elif option == '2':
        print("\nExiting... Thank You! Visit Again")

    else:
        print("\nInvalid Option!")

except Exception as e:
    print("\n⚠ Unexpected Error:", str(e))

print("\nMade with ❤️ by Amit M")
print("© 2025 All Rights Reserved")
print("Thank You!")









