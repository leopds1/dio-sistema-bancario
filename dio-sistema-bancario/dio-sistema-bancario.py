menu = """

[d] Deposit
[w] Withdraw
[s] Statement
[q] Quit

=> """

balance = 0
limit = 500
statement = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Enter the deposit amount: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: R${amount:.2f}\n"
            print("Deposit successful.")
        else:
            print("Operation failed! The amount entered is invalid.")

    elif option == "w":
        amount = float(input("Enter the withdrawal amount: "))

        exceeded_balance = amount > balance
        exceeded_limit = amount > limit
        exceeded_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operation failed! You don't have enough balance.")

        elif exceeded_limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")

        elif exceeded_withdrawals:
            print("Operation failed! Maximum number of withdrawals exceeded.")

        elif amount > 0:
            balance -= amount
            statement += f"Withdrawal: R${amount:.2f}\n"
            number_of_withdrawals += 1
            print("Withdrawal successful.")
        else:
            print("Operation failed! The amount entered is invalid.")

    elif option == "s":
        print("\n================ STATEMENT ================")
        print("No transactions have been made." if not statement else statement)
        print(f"\nBalance: R${balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select the desired operation again.")
