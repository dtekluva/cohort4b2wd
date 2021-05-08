# #Calculating Total Amopunt Payable, Simple Interest

# def simple_interest(P, R, T):
#     SI = (P * R * T)/100
#     return SI

# P = int(input("Enter Principal amount : "))
# R = int(input("Enter the rate on investment : "))
# T = int(input("Enter the duration of investment : "))

# SI = simple_interest(P, R, T)

# print("Simple interest : {}". format(SI))

# def total_amount_payable(SI):
#     Profit = SI + P
#     return Profit
# Profit = total_amount_payable(SI)

# print("Total Amount Payable :{}". format(Profit))


#Formaular to aid the distribution of Sweets amongst Friends

def love_sharing_formular(A, B, C):
    LSF = (A + B + C)//3
    return LSF
A = int(input("Enter value for the first sweet brought in : "))
B = int(input("Enter value for the Second sweet brought in : "))
C = int(input("Enter value for the third Sweet brought in : "))

LSF = love_sharing_formular(A, B, C)

def crushed_value(A, B, C):
    Crushed = (A + B + C)%3
    return Crushed
Crushed = crushed_value(A, B, C)


print(f'"Hello guys, Each of you should get {LSF} sweets and {Crushed} should be crushed')

    