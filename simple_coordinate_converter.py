#!/usr/bin/python3

# Copyright 2016 Francisco Pina Martins <f.pinamartins@gmail.com>
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

# Most of the code was taken from here: <http://en.proft.me/2015/09/20/converting-latitude-and-longitude-decimal-values-p/>
# Usage:python3 simpe_coordinate_converter.py coords.csv

import re

def dms2dd(degrees, minutes, seconds, direction):
    """
    Convert DMS coordinates to decimal degrees
    """
    decdeg = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    if direction == 'S' or direction == 'W':
        decdeg *= -1

    return str(round(decdeg, 4))


def parse_dms(dms):
    parts = re.split('[^\dESNW]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    lng = dms2dd(parts[4], parts[5], parts[6], parts[7])

    return (lat, lng)


def main(coords_filename):
    """
    Reads the DMS values from a CSV file and outputs the converted values to
    STDOUT. Assumes a header, tab delimiters and the order "ID LAT LON".
    """
    infile = open(coords_filename, 'r')
    header = infile.readline() # Skip header
    print(header, end="")
    for lines in infile:
        data = lines.split()
        label = data[0]
        decdeg = parse_dms("\t".join(data[1:]))
        print(label + "\t" + "\t".join(decdeg))


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
