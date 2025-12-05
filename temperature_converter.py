# Temperature conversion calculator 

Temperature = float(input("Enter temperature:"))
Unit = input("Enter unit celsius or fahrenheit (C/F):")
if Unit == "C":
    Unit = (Temperature * 9/5) + 32, "F"
elif Unit == "F":
    Unit = (Temperature - 32) * 5/9
else:
    print("invalid unit")
print(f"the converted {Temperature} is {Unit}")