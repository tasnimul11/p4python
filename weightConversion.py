#Python Kilogram to Pound Weight Converter

weight = float(input("What is your weight?: "))
unit = input("Kilogram(Kg) or Pound(Lb)? (Press K / L): ")

if unit == "K" or "k":
    weight = weight * 2.205  #converts KG to Pound(Lbs)
    print(f"Your weight is {weight} Lbs.") 

elif unit == "L" or "l":
    weight = weight / 2.205  #converts Pound to KG
    print(f"Your weight is {weight} Kg.")

else:
    print(f"Your {unit} is NOT VALID")