# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def get_valid_float(prompt):
    """Prompt the user for a valid float value."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_int(prompt):
    """Prompt the user for a valid integer value."""
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Savings Account Details:")
    savings_balance = get_valid_float("Enter the initial balance for the savings account: ")
    savings_interest_rate = get_valid_float("Enter the annual interest rate (in %) for the savings account: ")
    savings_months = get_valid_int("Enter the number of months for the savings account: ")

    # Call the create_savings_account function and pass the variables from the user.
    savings_updated_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest_rate, savings_months
    )

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("\nSavings Account Summary:")
    print(f"Initial Balance: ${savings_balance:.2f}")
    print(f"Interest Rate (Annual): {savings_interest_rate:.2f}%")
    print(f"Duration: {savings_months} months")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Balance: ${savings_updated_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("\nCD Account Details:")
    cd_balance = get_valid_float("Enter the initial balance for the CD account: ")
    cd_interest_rate = get_valid_float("Enter the annual interest rate (in %) for the CD account: ")
    cd_months = get_valid_int("Enter the number of months for the CD account: ")

    # Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("\nCD Account Summary:")
    print(f"Initial Balance: ${cd_balance:.2f}")
    print(f"Interest Rate (Annual): {cd_interest_rate:.2f}%")
    print(f"Duration: {cd_months} months")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated Balance: ${cd_updated_balance:.2f}")


if __name__ == "__main__":
    main()
