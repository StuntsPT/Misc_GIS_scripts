#!/usr/bin/python3

from __future__ import division
from osgeo import gdal
from collections import OrderedDict
import numpy as np


def get_value_at_point(rasterfile, pos):
    gdata = gdal.Open(rasterfile)
    gt = gdata.GetGeoTransform()
    data = gdata.ReadAsArray().astype(np.float)
    gdata = None
    x = int((pos[0] - gt[0])/gt[1])
    y = int((pos[1] - gt[3])/gt[5])
    return data[y, x]

def read_shapefile(shapefile_name):
    shapes = open(shapefile_name, 'r')
    shapes.readline() # Skip header
    coords = OrderedDict()
    for lines in shapes:
        lines = lines.split()
        coords[lines[0]] = tuple(map(float, lines[1:3][::-1]))
    
    shapes.close()
    return coords 

#p = (-8.31622, 43.50084)
#print(get_value_at_point('bio10_15', p))


if __name__ == "__main__":
    from sys import argv
    coords = read_shapefile(argv[1])
    print("Sample\t" + "\t".join(argv[2:]))
    for ind in coords.keys():
        print(ind, end="\t")
        for files in argv[2:]:
            print(get_value_at_point(files, coords[ind]), end="\t")
        print()
