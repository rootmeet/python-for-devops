import sys

# this is conditional handling
input = sys.argv[1]

if input == "t2.micro":
    print("This %s will charge you 20INR/hr"% input)
elif input == "t2.medium":
    print("This {0} will charge you 40INR/hr".format(input))
elif (input == "t2.large" or input == "t2.xlarge"):
    print(f"This {input} will charge you 100INR/hr")
else:
    print("Your input is not valid")

