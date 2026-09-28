#Mini-project_001 Dream job predictor

name = input("Enter the name:")
month = input("Enter your birth month:")

print("/n your dream job is:")

if month.lower() == "january":
    print("Ai Engineer")
elif month.lower() == "febuary":
    print("Fashion Designer")
elif month.lower() == "march":
    print("Developer")
else:
    print("Content Creator")