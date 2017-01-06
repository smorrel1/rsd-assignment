#!/usr/bin/env python3
# mock to test default parameters passed to requests.get in greengraph
from mock import patch
from greengraph.greengraph import *
def test_greengraph_func_mock():
  with patch('geopy.geocoders.GoogleV3.geocode') as mock_get:
    mygraph = greengraph_func(steps=2)
    mock_get.assert_called_with(
      "http://maps.googleapis.com/maps/api/staticmap?",
      params={
        'sensor': 'false',
        'zoom': 12,
        'size': '400x400',
        'center': '51.0,0.0',
        'style': 'feature:all|element:labels|visibility:off'
      }
    )


test_greengraph_func_mock()