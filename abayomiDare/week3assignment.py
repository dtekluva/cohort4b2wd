# 1. Write a program that takes in 2 numbers, a dividend and a divisor and prints out the result from the division and the rremainder as such

# >> Enter dividend : 7
# >> Enter divisor : 3

# >> 2 remainder 1


user_first_input = int(input('Enter dividend:\n'))
user_second_input = int(input('Enter divisor:\n'))
soln_without_remainder = user_first_input // user_second_input
remainder = user_first_input % user_second_input

print(f'{soln_without_remainder} remainder {remainder}')





