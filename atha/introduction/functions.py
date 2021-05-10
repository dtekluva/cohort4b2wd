# def volts(current):

#     resistance = int(input("Please enter resistance : "))

#     return current * resistance

# def power(volts, current):
    
#     return volts * current

# current = int(input("Please enter current : "))

# voltage = volts(current)

# power = power(voltage, current)
# print(power)


def voltage(resistance, current):

    voltage = int(resistance * current)
    return voltage

insert_value_resistance = resistance = float(input("Please insert value : "))
insert_value_current = current = float(input("Please insert value : "))
voltage = voltage(resistance, current)

def power(voltage, Current):

    power = int(voltage * Current)
    return power

insert_value_Current = Current = float(input("Please insser vlaue : "))
power = power(voltage, Current)

print(power, "watts")
print(voltage, "volts")