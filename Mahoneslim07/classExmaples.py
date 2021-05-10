
# def love_sharing_formular(A, B, C):
#     LSF = int((A + B + C)//3)
#     return LSF
# A = float(input("Enter value for the first sweet brought in : "))
# B = float(input("Enter value for the Second sweet brought in : "))
# C = float(input("Enter value for the third Sweet brought in : "))

# LSF = love_sharing_formular(A, B, C)

# def crushed_value(A, B, C):
#     Crushed = int((A + B + C)%3)
#     return Crushed
# Crushed = crushed_value(A, B, C)

# print(f'Hello guys, Each of you should get {LSF} sweets and {Crushed if Crushed > 0 else "None"} should be crushed')




def simple_interest(P, R, T):
    SI = int((P * R * T)/100)
    return SI

principla_value = P = float(input("Enter Principal amount : "))
rate_value = R = float(input("Enter the rate on investment : "))
duration_value = T = float(input("Enter the duration of investment : "))

SI = simple_interest(P, R, T)

print(f"Simple interest : {SI}")

def total_amount_payable(SI):
    Profit = int(SI + P)
    return Profit
Profit = total_amount_payable(SI)

print(f"Total Amount Payable :{Profit}")