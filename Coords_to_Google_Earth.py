#!/usr/bin/python3

def local_parser(locfilename):
    """
    Pareses a csv file with "name", "Latitude", "Longitude" and "Altitude"
    and returns a dict with this information.
    """
    with open(locfilename, 'r') as infile:
        data = {}
        for lines in infile:
            lines = lines.strip().split(",")
            data[lines[0]] = lines[1:]

    return data


def write_kml(kmlfilename, data):
    """
    Takes the data from the "local_parser" and a target file and writes a new
    kml document. Don't forget to zip it and rename it to ".kmz" to use in
    Google Earth.
    """
    with open(kmlfilename, 'w') as outfile:
        static1 = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>Untitled Placemark.kmz</name>
	<StyleMap id="m_ylw-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#s_ylw-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#s_ylw-pushpin_hl</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="s_ylw-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
	<Style id="s_ylw-pushpin_hl">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
	</Style>
"""
        static2 = """</Document>
</kml>"""
        placemark_static = """		<LookAt>
			<longitude>-8.784782785567524</longitude>
			<latitude>38.96530053129258</latitude>
			<altitude>0</altitude>
			<heading>2.148916314834085e-08</heading>
			<tilt>0</tilt>
			<range>667011.4659444446</range>
			<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
		</LookAt>
		<styleUrl>#m_ylw-pushpin</styleUrl>
		<Point>
			<gx:drawOrder>1</gx:drawOrder>
"""
        placemark_end = """		</Point>
	</Placemark>
"""

        outfile.write(static1)
        for k in data:
            name = "\t<Placemark>\n\t\t<name>" + k + "</name>\n"
            outfile.write(name)
            outfile.write(placemark_static)
            coords = "\t\t\t<coordinates>" + ",".join(data[k]) + "</coordinates>\n"
            outfile.write(coords)
            outfile.write(placemark_end)
        outfile.write(static2)

if __name__ == "__main__":
    # Usage: python3 places.py coords.csv file.kml
    from sys import argv
    data = local_parser(argv[1])
    write_kml(argv[2], data)
