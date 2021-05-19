def volts(current):

    resistance = int(input("Please enter resistance : "))

    return current * resistance
5
def power(volts, current):
    
    return volts * current

current = int(input("Please enter current : "))

voltage = volts(current)

power = power(voltage, current)
print(power)