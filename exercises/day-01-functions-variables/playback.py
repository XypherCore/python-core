# playback.py: Playback Speed (CS50P Problem Set 0)
# https://cs50.harvard.edu/python/2022/psets/0/playback/
#
# Task: prompt the user for text and print it with the words joined by "...".
# Note: split() collapses repeated spaces and drops leading/trailing ones,
# so "a  b" prints as a...b, not a......b.
#
# Example:
#   input:  This is CS50
#   output: This...is...CS50

s = input()
print(*s.split(), sep="...")