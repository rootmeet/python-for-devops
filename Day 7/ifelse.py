import sys

input = sys.argv[1]

if input == "t2.micro":
    print("This t2.micro will charge you 20INR/hr")
elif input == "t2.medium":
    print("This t2.medium will charge you 40INR/hr")
elif input == "t2.large":
    print("This t2.large will charge you 100INR/hr")
else:
    print("Your input is not valid")

