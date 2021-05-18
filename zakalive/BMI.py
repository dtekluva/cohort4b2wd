height = float(input("Please enter height in CM :"))
weight = float(input("Please enter weight in KG :"))

# to perform calculations with the input string we convert it to float
# BMI = kg/m^2

BMI = weight / (height/100)**2

print(f"YOUR BMI = {BMI}")

# 18.4 or < = underweight
# 18.5 - 24.9 = regular weight
# 25 - 29.9 = over weight
# 30 - 34.9 = obesity class 1
# 35 - 39.9 = obesity class 2
# 40 - ^^^^ = obesity class 3

if BMI <= 18.4: 
    print("YOU ARE UNDERWEIGHT MY GUY")
elif BMI <= 24.9:
    print("YOU ARE HEALTHY")
elif BMI <= 29.9:
    print("YOU NEED TO WATCH YOUR WEIGHT, IT IS GETTING OUT OF HAND")
elif BMI <= 34.9:
    print("OMO!! YOU NEED TO CALM DOWN COS YOU ARE OBESE")
elif BMI <= 39.9:
    print("OMOx1000!! THIS IS DANGEROUS COS YOU ARE OBESE!!")
else:
    print("ERROR! ERROR!! ERROR!!!") 
