""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest = interest_rate

    # Get balance
    def get_balance(self):
        """Returns the current balance of the account."""
        return self.balance
    
    # This method sets the balance of the account.   
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # Get interest
    def get_interest(self):
        """Returns the interest rate."""
        return self.interest
    
    # The method sets the interest gained for the account.
    def set_interest(self, interest_rate):
        """Sets the interest gained for the the account"""
        self.interest = interest_rate
