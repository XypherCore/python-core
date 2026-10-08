# tip.py: Tip Calculator (CS50P Problem Set 0)
# https://cs50.harvard.edu/python/2022/psets/0/tip/
#
# Task: prompt for a meal cost like "$50.00" and a tip percentage like "15%",
# then print the tip to two decimal places.
#   dollars_to_float("$50.00") -> 50.0
#   percent_to_float("15%")    -> 0.15
#
# Example:
#   input:  $50.00, 15%
#   output: Leave $7.50

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.removeprefix("$"))


def percent_to_float(p):
    return float(p.removesuffix("%"))/100

main()