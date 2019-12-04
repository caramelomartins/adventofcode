import math

basic = 0
total = 0

def calculate_fuel(mass):
    return math.floor(mass / 3) - 2 if mass else 0

def calculate_fuel_of_fuel(mass):
    fuel = calculate_fuel(mass)
    print("Fuel Requirement: {}.".format(fuel))

    if fuel > 0:
        return fuel + calculate_fuel_of_fuel(fuel)
    else:
        return 0


def calculate():
    global basic
    global total

    with open("input.txt") as file:
        for line in file.readlines():
            mass = int(line)

            fuel = calculate_fuel(mass)
            print("Fuel: {}.".format(fuel))
            basic += fuel

            extra = calculate_fuel_of_fuel(fuel)
            print("Extra Fuel: {}.".format(extra))
            total += fuel + extra


calculate()

print()
print("Basic: {}.".format(basic))
print("Total: {}.".format(total))
