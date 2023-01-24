'''
EXCEPTIONS

Bank ATM

This exception handling scenario deals with the exceptional cases that arise in the ATM of a bank.

About the ATM

This is a special kind of ATM that takes three integer inputs from the user, one-by-one. They are:

1. balance - Current Balance of the account.

2. choice - Choice of purpose, that is, Deposit(1) or Withdrawal(2).

3. amount - Amount of Deposit or Withdrawal.

Write the function definition for the function 'Bank_ATM', that takes 3 parameters, which are the above 3 inputs. 

Do the following in order

1. Check for the balance and  Raise ValueError exception if the input for the current balance is less than '500' and Print the Message. The message to the user must be, "As per the Minimum Balance Policy, Balance must be at least 500"
The input for the option 'choice' will be either '1' or '2', '1' is for Deposit, and '2' is for Withdrawal.

2. Based on the choice, if the choice is 1, check for the amount value parameter to be deposited and Raise a User-Defined exception "MinimumDepositError" if the input for the deposit amount is less than '2000', and Print the Message. The message to the user must be, "The Minimum amount of Deposit should be 2000"

else

'Add' the deposit amount to the "Balance".

3. Based on the choice, if the choice is 2, check for the amount value parameter to be withdrawn and Raise a User-Defined exception "MinimumBalanceError", if the balance amount after withdrawal is less than '500', and Print the Message. The message to the user must be, "You cannot withdraw this amount due to Minimum Balance Policy"

else

'Subtract' the withdrawn amount from the "Balance".

 

If any transaction has taken place without any exception 

4. Print the updated balance as "Updated Balance Amount is 5500"

 

Important Note

1. The user-defined exception names should be the same as given above.

2. The class definition for the user-defined exceptions must be done Above the Function definition of 'Bank_ATM'. 
'''

#CODE STUB

#Define the Class for user-defined exceptions "MinimumDepositError" and "MinimumBalanceError" here
# define MinimumDepositError
class MinimumDepositError(Exception):
  def __init__(self):
		self.msg = "The Minimum amount of Deposit should be 2000"
		super().__init__(self.msg)


#define MinimumBalanceError
class MinimumBalanceError(Exception):
  def __init__(self):
        self.msg = "You cannot withdraw this amount due to Minimum Balance Policy"
        super().__init__(self.msg)

#Complete the 'Bank_ATM' function below.
def Bank_ATM(balance,choice,amount):
    # Write your code here
    # check balance, raise ValueError exception if the input for the current balance is less than '500'
    if balance < 500:
        msg = "As per the Minimum Balance Policy, Balance must be at least 500"
        raise ValueError(msg)

    # deposit
    if choice == 1:
        if amount < 2000:
            raise MinimumDepositError
        else:
            new = balance + amount
            print(f"Updated Balance Amount: {new}")

    # withdrawal
    if choice == 2:
        if balance - amount < 500:
            raise MinimumBalanceError
        else:
            new = balance - amount
            print(f"Updated Balance Amount: {new}")
 

if __name__ == '__main__':
    
    bal = int(input())
    ch = int(input())
    amt = int(input())
    
    try:
        Bank_ATM(bal,ch,amt)
    
    
    except ValueError as e:
        print(e)
    except MinimumDepositError as e:
        print(e)
    except MinimumBalanceError as e:
        print(e)
