# Misc_GIS_scripts
A place to store my scripts involving GIS data.

## layer_data_extractor.py

Script to extract the values of a rasterfile in a list of provided coordinates.
Requires a shapefile and rasterfiles.

### Usage:

```
python layer_data_extractor.py shapefile.csv rasterfile(s)
```

The "shapefile.csv" should have a header and the following data: LABEL LAT LON.
The separator can be any number of spaces and/or tabs.
Eg:

```
LABEL   LAT LON
Ind.1   41.6611 -7.8747
Ind.2   43.4997 -8.3164
Ind.3   39.5677 -6.6573
```


The rasterfile(s) can be globed in the shell or provided one by one.
The output is sent to STDOUT.

### Example usages:

```bash
python layer_data_extractor.py ~/shapefile.csv ~/GIS_data/BioClim1.bil ~/GIS_data/BioClim2.bil

python layer_data_extractor.py ~/shapefile.csv ~/GIS_data/*.bil
```

### Requirements:

This script requires the package [python-gdal](https://pypi.python.org/pypi/GDAL/) to work.

## Coords_to_Google_Earth.py

This is a **very** dirty hackish script to get a coordinate file and produce a Google Earth input file with place-marks.

### Usage:

Format a csv with coordinates:

```
Sample name, Longitude, Latitude, Altitude
```

Just use the program like so:

```bash
python3 Coords_to_Google_Earth.py coords.csv new_file.kml
```

And you are good to go.

## simple_coordinate_converter.py

This script will convert a csv file wing tabs as separators with DMS coordinates into decimal coordinates. It outputs to STDOUT.

### Usage:

Format a csv with DMS coordinates:

```
Sample name, Latitude, Longitude
```

```bash
python3 python3 simpe_coordinate_converter.py coords.csv > output_file.csv
```

That's really all there is to it...

## License

GPL V3
