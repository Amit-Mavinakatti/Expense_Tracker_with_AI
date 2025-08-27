from openai import OpenAI

print("\n\n\n=============================================:Expense Tracker:============================================\n")
print("\n")
print("Hey WelCome!")
print("\n")
print("Here's our simple tool Expense Tracker. \nHere you can take look on managing and working on your expenses .")
print("Let's GO....")
print("\n")
print("Fill the following to proceed :")
print("\n")

try:
    name = input("User Name: ")
    print("\n")
    Email = input("Email    : ")
    print("\n")
    password = input("Password : ")
    print("\n")

    while True:
        try:
            income = int(input("Enter Your Monthly Earnings:(in Rs.) "))
            break
        except ValueError:
            print("❌ Please enter a valid number for income. Try again!\n")
    print("\n")

    secured = "#####" + str(password[-1]) if password else "#####"

    print("====================================================:Expense Tracker:==========================================\n")
    print("\nAccount Details :\n")
    print("\nUSER NAME :", name.upper())
    print("\nEmail     :", Email.upper())
    print("\nPassword  :", secured)
    print("\nTOTAL INCOME : ", income)

    expenses_list = []
    budget_list = []

    print("=========================================:Main Menu:=====================================")

    print("\n1) Lets Start")
    print("2) Exit ")

    print("\n\n Our Tool also has  AI Feature , if you want to Use our AI just follow the procedures:")
    print(" * Press 'AI' To Enetr AI Mode\n")
    print(" *Enter 'quit' to Exit from AI Mode\n")
    option = input("\nEnter Your option: ")

    if option == '1':
        print("\nOops! you don't have any Expenses yet!")
        print("\nDo u want to add new expenses?(y/n)")
        option2 = input("Enter Here: ")
        print("\n")

        if option2.lower() == 'y':
            while True:
                try:
                    num = int(input("How many Expenses do you want to add? : "))
                    break
                except ValueError:
                    print("❌ Please enter a valid number!\n")

            print("\nEnter " + str(num) + " New Expenses\n")

            for i in range(num):
                expenses = input("Enter: ")
                expenses_list.append(expenses)

            print("\nHere are your Expenses :")
            for i in range(len(expenses_list)):
                print(str(i + 1) + ") " + expenses_list[i])

            print("\nDo You want to add Budget for your expenses?(y/n)")
            option3 = input("Enter: ")
            print("\n")

            if option3.lower() == 'y':
                for i in range(len(expenses_list)):
                    while True:
                        try:
                            print("Add budget for " + expenses_list[i] + "( in Rs.)")
                            budget = int(input("Your Budget:(in Rs.) "))
                            budget_list.append(budget)
                            print("Budget for " + expenses_list[i] + " is = Rs. " + str(budget_list[i]))
                            print("\n")
                            break
                        except ValueError:
                            print("❌ Please enter a valid number for budget.\n")

            print("Please press = for Our tracker Suggestions:")  
            sug = input("Your entry: ")

            if sug == '=':
                print("Getting Summary from  Tracker ......................\n")
                print("\n=============== Here is Summary of Your Expenses ==========================: \n")

                print("Expenses" + "   " + "Budget(in Rs.)\n")

                for a, b in zip(expenses_list, budget_list):
                    print(f"{a} = {b}")

                print("\n1) Your Total expenses are     : ", len(expenses_list))
                print("2) Your Total income is Rs.      : ", income)
                print("3) Your Total budget is Rs       : ", sum(budget_list))
                if budget_list:  # Prevent error if no budget entered
                    print("4) Highest Budget is   Rs.       : ", max(budget_list))
                    print("5) Lowest Budget is    Rs.       : ", min(budget_list))
                print("\n")

                if income > sum(budget_list):
                    print("Don't Worry ! Your Expenses are in good range:")
                    print("Keep it up.")
                else:
                    print("Alert !! Your Expenses utility is GREATER than your monthly earnings :")
                    print("Pro tip: Try to minimize the expenses")

                print("\nThank You\nVisit Again")

    elif option == 'AI':
        print("\n==========================================================: AI Mode :================================================================")
        print("*Enter 'quit' to exit from the AI Mode")
        try:
            client = OpenAI(api_key="")  # ⚠ Replace with your actual key
            while True:
                user_input = input("You : ")
                if (user_input.lower() in ['quit', "bye", "exit"]):
                    print("Exiting.....")
                    print("Thank YOU!")
                    break
                try:
                    response = client.responses.create(
                        model='gpt-4.1-mini',
                        input=user_input
                    )
                    print("AI: ", response.output_text, "\n")
                except Exception as e:
                    print("⚠️ AI Error:", str(e))
        except Exception as e:
            print("⚠️ Could not start AI Mode:", str(e))

    elif option == '2':
        print("\nExiting..............")
        print("Thank You!\nVisit Again")

    else:
        print("\nInvalid Option!!")

except Exception as e:
    print("\n⚠️ An unexpected error occurred:", str(e))

print("\nMade with Love")
print("CopyRight 2025 ")
print("All Rights Reserved")
print("Creator : Amit")
print("Contact : 9353912665")
