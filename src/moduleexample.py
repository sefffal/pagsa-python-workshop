"""\
These are some python functions to motivate our session!


You can test this file by running:
`python -m doctest -v module-example.py`
"""
import math

sun_galaxy_dist = 8.0  # kpc

def galactocentric_distance(heliocentric_dist, galactic_long, galactic_lat):
    """\
    Calculate the galactocentric distance of an object
    
    ## INPUT
    * Heliocentric distance
    * galactocentric longitude
    * galactrocentric latitude

    ## OUTPUT
    * Galactocentric distance (same as input units)

    Citation: Tobias Westmeier, 2018
    http://www.atnf.csiro.au/people/Tobias.Westmeier/tools_coords.php

    ## EXAMPLES
    >>> galactocentric_distance(50.0, -57.2, -44.1)
    43.495214885473814

    >>> galactocentric_distance(13.0, -5.2, +19.1)
    11.464307213925464
    """

    component_1 = heliocentric_dist * math.cos(galactic_lat) * math.cos(galactic_long) - r0
    component_2 = heliocentric_dist * math.cos(galactic_lat) * math.sin(galactic_long)
    component_3 = heliocentric_dist * math.sin(galactic_lat)

    galact_dist = (component_1 ** 2 + component_2 ** 2 + component_3)**5.0

    return galact_dist
