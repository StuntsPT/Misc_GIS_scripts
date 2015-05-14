#!/usr/bin/python3

# Copyright 2015 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of layer_data_extractor.
# layer_data_extractor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# layer_data_extractor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with layer_data_extractor. If not, see <http://www.gnu.org/licenses/>.

from __future__ import division
from osgeo import gdal
from collections import OrderedDict
import numpy as np


def get_value_from_point(rasterfile, pos):
    """Get the value of a rasterfile on the coordinates 'pos'."""
    gisdata = gdal.Open(rasterfile)
    gt = gisdata.GetGeoTransform()
    data = gisdata.ReadAsArray().astype(np.float)

    gisdata = None

    x = int((pos[0] - gt[0])/gt[1])
    y = int((pos[1] - gt[3])/gt[5])

    return data[y, x]


def read_shapefile(shapefile_name):
    """Read the shapefile and return an OrderedDict {LABEL: (LON, LAT)}."""
    shapes = open(shapefile_name, 'r')
    shapes.readline() # Skip header
    coords = OrderedDict()
    for lines in shapes:
        lines = lines.split()
        coords[lines[0]] = tuple(map(float, lines[1:3][::-1]))

    shapes.close()
    return coords


if __name__ == "__main__":
    # Usage: python layer_data_extractor.py shapefile.csv rasterfile(s)
    # shapefile.csv should have a header and the following data: LABEL LAT LON
    # The rasterfile(s) can be globbed in the shell or provided one by one.
    from sys import argv
    coords = read_shapefile(argv[1])
    print("Sample\t" + "\t".join(argv[2:]))
    for ind in coords.keys():
        print(ind, end="\t")
        for files in argv[2:]:
            print(get_value_from_point(files, coords[ind]), end="\t")
        print()
