# Greengraph plots a line showing the percentage of green pixels between
# two points.  Copyright (C) 2016 Stephen Morrell. See LICENCE for details.

import yaml
import os
from ..greengraph import greengraph_func
from nose.tools import assert_equal
import ..geolocate

def test_greengraph_func():
london_location = geolocate("London")
assert_equal(london_location, [51.5073509, -0.1277583])
