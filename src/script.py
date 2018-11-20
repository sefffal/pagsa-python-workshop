"""\
This is a script for us to play around with in our demos!
"""
__author__ = "William Thompson"

from moduleexample import galactocentric_distance


d1 = galactocentric_distance(12.0, -19.0, +120.0)

print(f"The distance from the centre of the galaxy is {d1:.2f}")
