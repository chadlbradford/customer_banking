"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class
    savings_account = Account(balance=balance, interest_rate=0)

    # Calculate interest earned
    monthly_interest_rate = interest_rate / 12
    savings_interest_earned = savings_account.get_balance() * (monthly_interest_rate / 100) * months

    # Update the savings account balance
    savings_updated_balance = savings_account.get_balance() + savings_interest_earned
    savings_account.set_balance(savings_updated_balance)

    # Set interest earned
    savings_account.set_interest(savings_interest_earned)

    # Return the updated balance and interest earned
    return savings_updated_balance, savings_interest_earned
