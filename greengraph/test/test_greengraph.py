#!/usr/bin/env python
#  Greengraph plots a line showing the percentage of green pixels between
# two points.  Copyright (C) 2016 Stephen Morrell. See LICENCE for details.

import yaml
import os
from greengraph.greengraph import *
from nose.tools import assert_equal  # , assert_list_equal, assert_almost_equal, assert_sequence_equal
from numpy.testing import assert_array_equal
def test_func():

  # test geolocate
  myGG = Greengraph('London', 'Oxford')
  london_location = myGG.geolocate("London")
  assert_equal(london_location, (51.5073509, -0.1277583))

  # test location_sequence
  mySequence = myGG.location_sequence([51., 0.], [52., 1.], 3)  # ndarray
  answer = [[51., 0.], [51.5, 0.5], [52., 1.]]  # tuple
  assert_array_equal(answer, mySequence, err_msg='location_sequence failed')

  # test green_between


  # test greengraph_func
  with open(os.path.join(os.path.dirname(__file__),
              'fixtures', 'samples.yaml')) as fixtures_file:
    fixtures = yaml.load(fixtures_file)
    for fixture in fixtures:
      answer = fixture.pop('answer')
      assert_equal(greengraph_func(**fixture), answer)

if __name__ == '__main__':
  test_func()