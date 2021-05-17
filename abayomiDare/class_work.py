import math


b_input = int(input('input B:\n'))
square_b_input = b_input ** 2
a_input = int(input('input A :\n'))
c_input = int(input('input c :\n'))

root_soln = square_b_input - 4 * a_input * b_input

new_root_soln = root_soln ** 0.5

division_stage = new_root_soln / (2 * a_input)


stage1 = - b_input - division_stage
stage2 = - b_input + division_stage


print(stage1)
print(stage2)

