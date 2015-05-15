# Misc_GIS_scripts
A place to store my scrpits involving GIS data

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


The rasterfile(s) can be globbed in the shell or provided one by one.
The output is sent to STDOUT.

### Example usages:

```bash
python layer_data_extractor.py ~/shapefile.csv ~/GIS_data/BioClim1.bil ~/GIS_data/BioClim2.bil

python layer_data_extractor.py ~/shapefile.csv ~/GIS_data/*.bil
```

## License

GPL V3
