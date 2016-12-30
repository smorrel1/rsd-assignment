#!/usr/bin/env python
# TODO: change top level directory from rsd-assignment to greengraph
import numpy as np
import geopy
from io import StringIO
from matplotlib import image as img
from matplotlib import pyplot as plt
import requests
import sys
import argparse

class Greengraph(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

  def geolocate(self, place):
    return self.geocoder.geocode(place, exactly_one=False)[0][1]

  def location_sequence(self, start, end, steps):
    lats = np.linspace(start[0], end[0], steps)
    longs = np.linspace(start[1], end[1], steps)
    return np.vstack([lats, longs]).transpose()

  def green_between(self, steps):
    return [Map(*location).count_green()
            for location in self.location_sequence(
                self.geolocate(self.start),
                self.geolocate(self.end),
                steps)]


class Map(object):
  def __init__(self, lat, long, satellite=True,
               zoom=10, size=(400, 400), sensor=False):
    base = "http://maps.googleapis.com/maps/api/staticmap?"
    params = dict(
      sensor=str(sensor).lower(),
      zoom=zoom,
      size="x".join(map(str, size)),
      center=",".join(map(str, (lat, long))),
      style="feature:all|element:labels|visibility:off")
    if satellite:
      params["maptype"] = "satellite"

    self.image = requests.get(base, params=params).content  # Fetch our PNG image data
    self.pixels = img.imread(StringIO(self.image))

  # Parse our PNG image as a numpy array
  def green(self, threshold):
    # Use NumPy to build an element-by-element logical array
    greener_than_red = self.pixels[:, :, 1] > threshold* self.pixels[:, :, 0]
    greener_than_blue = self.pixels[:, :, 1] > threshold*self.pixels[:, :, 2]
    green = np.logical_and(greener_than_red, greener_than_blue)
    return green

  def count_green(self, threshold=1.1):
    return np.sum(self.green(threshold))

  def show_green(self, threshold=1.1):  # changed data -> self because I think James' code was buggy
    green = self.green(threshold)
    out = green[:, :, np.newaxis] * np.array([0, 1, 0])[np.newaxis, np.newaxis, :]  # changed array -> np.array
    buffer = StringIO()
    result = img.imsave(buffer, out, format='png')
    return buffer.getvalue()

def greengraph_func():
  '''
  Plots a line showing the percentage of green pixels between two points

  Arguements
  ----------
  --from  Str   Origin location name
  --to    Str   Destination location name
  --steps int   Number of steps from origin to destination
  --out   Str   Output file name for graph in png format, e.g. graph.png

  Returns
  -------
  saves a graph as <name>.png
  '''
  args = sys.argv[1:-1]  # remove
  parser = argparse.ArgumentParser(description='Calculate greenery between two points.')
  parser.add_argument('--from', dest='start', type=str,
                      help='Origin location name.')
  parser.add_argument('--to', dest='end', type=str,
                      help='Destination location name')
  parser.add_argument('--steps', dest='steps', type=int,
                      help='Number of steps from origin to destination')
  parser.add_argument('--out', dest='output_file', type=str,
                      help='Output file name for graph in png format, e.g. graph.png')
  args = parser.parse_args()  # produces Namespace()
  print(args)  # remove
  mygraph = Greengraph(args.start, args.end)
  data = mygraph.green_between(args.steps)
  # save args.output_file  # TODO Save file to .png
  plt.plot(data)

if __name__ == '__main__':
  greengraph_func()