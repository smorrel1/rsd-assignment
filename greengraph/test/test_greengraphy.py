# Greengraph plots a line showing the percentage of green pixels between
# two points.  Copyright (C) 2016 Stephen Morrell. See LICENCE for details.

import yaml
import os
from greengraph.greengraph import *
from nose.tools import assert_equal
def test_func():
  # test geolocate
  myGG = Greengraph('London', 'Oxford')
  london_location = myGG.geolocate("London")
  assert_equal(london_location, (51.5073509, -0.1277583))
  # test greengraph_func
  with open(os.path.join(os.path.dirname(__file__),
              'fixtures', 'samples.yaml')) as fixtures_file:
    fixtures=yaml.load(fixtures_file)
    for fixture in fixtures:
      answer = fixture.pop('answer')
      assert_equal(greengraph_func(**fixture), answer)

if __name__ == '__main__':
  test_func()