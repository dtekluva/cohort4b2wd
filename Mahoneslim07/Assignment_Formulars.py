#Formular that Divides

def the_divider_value(d1, d2):
    D = d1//d2
    return D
dividend_value = d1 = int(input("Enter value of Dividend : "))
divisor_value = d2 = int(input("Enter value of Divisor : "))

D = the_divider_value(d1, d2)

def remainder_value(d1, d2):
    R = d1%d2
    return R
R = remainder_value(d1, d2)

print(f'{D} "remainder" {R}')

#Calculating Total Amopunt Payable, Simple Interest

def simple_interest(P, R, T):
    SI = (P * R * T)/100
    return SI

principla_value = P = float(input("Enter Principal amount : "))
rate_value = R = float(input("Enter the rate on investment : "))
duration_value = T = float(input("Enter the duration of investment : "))

SI = simple_interest(P, R, T)

print("Simple interest : {}". format(SI))

def total_amount_payable(SI):
    Profit = SI + P
    return Profit
Profit = total_amount_payable(SI)

print("Total Amount Payable :{}". format(Profit))

# #Formaular to aid the distribution of Sweets amongst Friends

def love_sharing_formular(A, B, C):
    LSF = (A + B + C)//3
    return LSF
A = float(input("Enter value for the first sweet brought in : "))
B = float(input("Enter value for the Second sweet brought in : "))
C = float(input("Enter value for the third Sweet brought in : "))

LSF = love_sharing_formular(A, B, C)

def crushed_value(A, B, C):
    Crushed = (A + B + C)%3
    return Crushed
Crushed = crushed_value(A, B, C)

print(f'Hello guys, Each of you should get {LSF} sweets and {Crushed} should be crushed')

    