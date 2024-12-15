# Customer Banking System

This project is a Python-based banking application that simulates the management of **Savings Accounts** and **Certificate of Deposit (CD) Accounts**. Users can input account details such as balance, interest rate, and duration (in months) to calculate the interest earned and the updated balance for each account.

## Features

1. **Account Management:**
   - Core functionality to create, update, and manage accounts.
   - Includes interest rate and balance management.

2. **Savings Account:**
   - Calculates interest earned over a specified duration.
   - Updates account balance with the earned interest.

3. **Certificate of Deposit (CD) Account:**
   - Computes interest earned for a fixed term.
   - Updates account balance at the end of the term.

4. **Interactive User Input:**
   - Prompts the user to input details for each account.
   - Displays the summary of account activity, including initial balance, interest earned, and final balance.

## File Structure

- `Account.py`:
  - Contains the `Account` class with methods to manage balance and interest rate.
- `savings_account.py`:
  - Implements the `create_savings_account` function for savings account interest calculation and balance updates.
- `cd_account.py`:
  - Contains the `create_cd_account` function to handle CD account logic.
- `customer_banking.py`:
  - The main script to interact with the user, process inputs, and display results.

## Usage

1. Clone this repository and ensure all the `.py` files are in the same directory.
2. Run the main script:
   ```bash
   python customer_banking.py
