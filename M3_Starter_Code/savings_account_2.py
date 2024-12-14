"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(initial_balance, interest_rate, months):
    # Step 1: Create an instance of the Account class
    savings_account.months = months
    savings_account = Account(balance=initial_balance, interest=interest_rate)    
    # Step 2: Calculate monthly interest rate
    monthly_rate = interest_rate / 12
    # Step 3: Calculate interest earned over the specified months
    interest_earned = balance * (monthly_rate * months)

    # Step 4: Add the interest earned to the account balance
    savings_account.set_balance(balance + interest_earned)

    # Step 5: Return the updated balance and interest earned
    return savings_account.balance, interest_earned   
 
    
    
"""Creates a savings account, calculates interest earned, and updates the account balance.

Args:
    balance (float): The initial savings account balance.
    interest_rate (float): The APR interest rate for the savings account.
    months (int): The length of months to determine the amount of interest.

Returns:
    float: The updated savings account balance after adding the interest earned.
    And returns the interest earned.
"""
# Create an instance of the `Account` class and pass in the balance and interest parameters.
#  Hint: You need to add the interest as a value, i.e, 0.
# ADD YOUR CODE HERE
balance = 1000  # Example balance
interest = 0.025  # Example interest (0 as per the hint)
months = 12  # Example months

# Instantiate the Account class
my_account = Account(balance, interest)

# Print details to confirm
print(f"Account created with balance: ${my_account.balance:.2f} and interest: {my_account.interest:.2f}")


# Calculate interest earned
# ADD YOUR CODE HERE
def calculate_apr(interest_earned, balance, months):
    """
    Calculates the Annual Percentage Rate (APR).

    Args:
        interest_earned (float): The total interest earned.
        balance (float): The initial account balance.
        months (int): The time period in months.

    Returns:
        float: The calculated APR as a percentage.
    """
    # Avoid division by zero
    if balance <= 0 or months <= 0:
        raise ValueError("Balance and months must be greater than zero.")
    
    # Calculate APR
    apr = (interest_earned / (balance * (months / 12))) * 100
    return apr


# Update the savings account balance by adding the interest earned
# ADD YOUR CODE HERE
updated_balance = balance + calculate_apr

# Print the updated balance for verification
print(f"Updated Savings Account Balance: ${updated_balance:.2f}")

# Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
# ADD YOUR CODE HERE

# Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
# ADD YOUR CODE HERE

# Return the updated balance and interest earned.
#return  # ADD YOUR CODE HERE  This return is giving errors.

