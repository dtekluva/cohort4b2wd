# num1 = int(input("Please enter num1 : "))
# num2 = int(input("Please enter num2 : "))

# quotient = num1//num2
# rem = num1%num2

# print(f"{quotient} remainder {rem}")

# p = float(input("Please enter principal : "))
# r = float(input("Please enter rate : "))
# t = float(input("Please enter time : "))

# i = (p *  r * t)/100

# print(f"Interest : {i}")
# print(f"Repayment amount : {i+p}")


friend1 = float(input("Please enter friend1 : "))
friend2 = float(input("Please enter friend2 : "))
friend3 = float(input("Please enter friend3 : "))

share = (friend1 + friend2 + friend3)//3
discard = share%3

print(f"HELLO GUYS, EACH OF YOU SHOULD GET {share}SWEETS AND {discard} SHOULD BE DISCARDED")