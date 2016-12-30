# Greengraph plots a line showing the percentage of green pixels between
# two points.  Copyright (C) 2016 Stephen Morrell. See LICENCE for details.

import yaml
import os
from ..greengraph import greengraph_func
from nose.tools import assert_equal
def test_greengraph_func():
    with open(os.path.join(os.path.dirname(__file__),
            'fixtures','samples.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            answer=fixture.pop('answer')
            assert_equal(greengraph_func(**fixture), answer)