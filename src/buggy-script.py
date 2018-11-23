"""\
This is a script for us to play around with in our demos!
"""
__author__ = "William Thompson"

from moduleexample import galactocentric_distance
from matplotlib import pyplot

d1 = galactocentric_distance(12.0, -19.0, +120.0)
print(f"The distance from the centre of the galaxy is {d1:.2f}")


# # Applying coordinates in a loop
# list_of_d = [19.1, +123.0]
# list_of_l = [45.8, -12.0]
# list_of_b = [119.0, -45.0]

# import numpy as np

# vgalactocentric_distance = np.vectorize(galactocentric_distance)

# d_list = vgalactocentric_distance(list_of_d, list_of_l, list_of_b)
# print(d_list)
# print()

gacl