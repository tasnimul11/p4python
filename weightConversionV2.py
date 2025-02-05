#Python Kilogram to Pound Weight Converter V2
#in this Version, we will use just 1 print function to show result

weight = float(input("What is your weight(just value)?: "))
unit = input("Kilogram(Kg) or Pound(Lb)? (Press K / L): ")

if unit == "K" or "k" or "KG" or "kg":
    weight = weight * 2.205  #converts KG to Pound(Lbs)
    unit = "Lbs."

elif unit == "L" or "l" or "Lb" or "LB":
    weight = weight / 2.205  #converts Pound to KG
    unit = "KG."

else:
    print(f"Your {unit} is NOT VALID")

print(f"Your weight is {round(weight, 2)} {unit}")