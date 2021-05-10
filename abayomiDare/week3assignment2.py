# assignment 2


# 2. PLEASE WRITE A SMALL PROGRAM THAT REQUESTS (USING THE INPUT BUILTIN FUNCTION) VALUES FOR (P) (R) AND (T).
#  AND SOLVES THE SIMPLE INTEREST AND PRINTS THE VALUE. ALSO PRINT THE TOTAL AMOUNT PAYABLE AT END OF PERIOD.

# Simple Interest= P x R x T ÷ 100, where P = Principal, R = Rate of Interest and T = Time Period of the Loan/Deposit in years.

def simple_interest():
    principal = input('Enter principal: ')
    rate = input('Enter rate: ')
    time = input('Enter time: ')
    try:
        principal = int(principal)
        rate = int(rate)
        time = int(time)
        amount_payable = principal + principal * rate * time
        sm_in = int(principal * rate * time / 100)
        return f'Simple interest = {sm_in}\n Total amount payable = {amount_payable}'
    except:
        principal = float(principal)
        rate = float(rate)
        time = float(time)
        amount_payable = principal + principal * rate * time
        sm_in = principal * rate * time / 100
        return f'Simple interest = {round(sm_in, 2)}\nTotal amount payable = {round(amount_payable, 2) }'


print(simple_interest())