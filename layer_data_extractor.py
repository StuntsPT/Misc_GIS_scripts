#!/usr/bin/python3

# Copyright 2015-2018 Francisco Pina Martins <f.pinamartins@gmail.com>
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

# Inspired by https://gis.stackexchange.com/a/46898

from collections import OrderedDict
from osgeo import gdal


def get_value_from_point(rasterfile, coords):
    """
    Open a rasterfile, read the data on the coordinates 'pos',
    and return that value.
    """
    gisdata = gdal.Open(rasterfile)
    trnsf = gisdata.GetGeoTransform()
    data = gisdata.GetRasterBand(1)

    for sample, crds in coords.items():
        x_coord = int((crds[0] - trnsf[0]) / trnsf[1])
        y_coord = int((crds[1] - trnsf[3]) / trnsf[5])

        intval = data.ReadAsArray(x_coord, y_coord, 1, 1)
        print('{}\t{}'.format(sample, intval[0][0]))


def read_shapefile(shapefile_name):
    """Read the shapefile and return an OrderedDict {LABEL: (LON, LAT)}."""
    shapes = open(shapefile_name, 'r')
    shapes.readline()  # Skip header
    coords = OrderedDict()
    for lines in shapes:
        lines = lines.split()
        coords[lines[0]] = tuple(map(float, lines[1:3][::-1]))

    shapes.close()
    return coords


if __name__ == "__main__":
    # Usage: python3 layer_data_extractor.py shapefile.csv rasterfile(s)
    # shapefile.csv should have a header and the following data: LABEL LAT LON
    from sys import argv
    COORDS = read_shapefile(argv[1])
    print("Sample\t" + "\t".join(argv[2:]))
    get_value_from_point(argv[2], COORDS)
