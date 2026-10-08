# faces.py: Making Faces (CS50P Problem Set 0)
# https://cs50.harvard.edu/python/2022/psets/0/faces/
#
# Task: convert(s) takes a string and returns it with ":)" replaced by 🙂
# and ":(" replaced by 🙁. main() prompts for input and prints the result.
#
# Example:
#   input:  Hello :)
#   output: Hello 🙂

def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

def main():
    print(convert(input()))
main()