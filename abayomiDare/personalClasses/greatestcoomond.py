# def gcd(x, y):
#     gcd = 1
    
#     if x % y == 0:
#         return y
    
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break  
#     return gcd

# print(gcd(12, 17))
# print(gcd(4, 6))

#or use the recursive method

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a%b)

print(greatest_common_divisor(64,48))
