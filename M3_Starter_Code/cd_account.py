"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: The updated CD account balance and the interest earned.
    """
    # Create an instance of the `Account` class
    cd_account = Account(balance=balance, interest_rate=0)

    # Calculate interest earned
    monthly_interest_rate = interest_rate / 12  # Convert annual rate to monthly
    cd_interest_earned = cd_account.get_balance() * (monthly_interest_rate / 100) * months

    # Update the CD account balance by adding the interest earned
    cd_updated_balance = cd_account.get_balance() + cd_interest_earned
    cd_account.set_balance(cd_updated_balance)

    # Set the interest earned
    cd_account.set_interest(cd_interest_earned)

    # Return the updated balance and interest earned
    return cd_updated_balance, cd_interest_earned
