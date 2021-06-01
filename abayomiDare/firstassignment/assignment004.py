
def area_of_a_circle(new_value_pie):
    user_input = input('please enter a radius value\n')
    convert = float(user_input)
    radius = convert ** 2
    return  f'Area of a circle with radius {convert} = {new_value_pie * radius} '

print(area_of_a_circle(3.142))
