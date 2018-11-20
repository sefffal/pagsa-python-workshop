"""\
These are some python functions to motivate our session!
"""
import numpy as np

sun_galaxy_dist = 8.0  # kpc

def galactocentric_distance(heliocentric_dist, galactic_long, galactic_lat):
    """\
    Calculate the galactocentric distance of an object from:
    * Heliocentric distance
    * galactocentric longitude
    * galactrocentric latitude

    Citation: Tobias Westmeier, 2018
    http://www.atnf.csiro.au/people/Tobias.Westmeier/tools_coords.php
    """

    galact_dist = np.sqrt(
        (heliocentric_dist * np.cos(galactic_lat) * np.cos(galactic_long) - r0) ** 2
        + (heliocentric_dist * np.cos(galactic_lat) * np.sin(galactic_long)) ** 2
        + (heliocentric_dist * np.sin(galactic_lat)) ** 2
    )

    return galact_dist

