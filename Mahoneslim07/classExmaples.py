
def love_sharing_formular(A, B, C):
    LSF = int((A + B + C)//3)
    return LSF
A = float(input("Enter value for the first sweet brought in : "))
B = float(input("Enter value for the Second sweet brought in : "))
C = float(input("Enter value for the third Sweet brought in : "))

LSF = love_sharing_formular(A, B, C)

def crushed_value(A, B, C):
    Crushed = int((A + B + C)%3)
    return Crushed
Crushed = crushed_value(A, B, C)

print(f'Hello guys, Each of you should get {LSF} sweets and {Crushed if Crushed > 0 else "None"} should be crushed')