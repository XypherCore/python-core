# einstein.py: Einstein (CS50P Problem Set 0)
# https://cs50.harvard.edu/python/2022/psets/0/einstein/
#
# Task: prompt for a mass in kilograms (integer) and print the equivalent
# energy in joules (integer) using E = m * c^2, with c = 300000000 m/s.
#
# Example:
#   input:  1
#   output: E: 90000000000000000

m = int(input("m (in kg): "))
c = 300000000
E = m*c**2
print(f"E: {E}")