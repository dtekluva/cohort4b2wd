
def user_input():
    user_first_name = input('input first name\n')
    reverse = user_first_name[::-1].upper()
    user_last_name = input('input last name\n')
    reverse_last_name = user_last_name[::-1].upper()
    return f"reversed order: \n {reverse}  {reverse_last_name}"


print(user_input())