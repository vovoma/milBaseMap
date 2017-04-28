import ogr #load ogr libraries
import geojson
from geojson import Feature, Point, FeatureCollection

# open ogr datasources and print out number of features
def open_shapefile(file_path):
	#define datasource
	datasource = ogr.Open(file_path)
	# define 1st layer in the datasource
	layer = datasource.GetLayerByIndex(0)

	# print out file path and number of features
	print("Opening {}".format(file_path))
	print("Number of features: {}".format(layer.GetFeatureCount()))

	# finish function and save result
	return datasource

def get_base_location(datasource):
	layer = datasource.GetLayerByIndex(0)
	base_locations = []
	layer.ResetReading()
	for feature in layer:
		point = feature.GetFieldAsString(3).split(" ")
		longtitude = float(point[1].split("(")[1])
		lattitude = float(point[2].split(")")[0])
		milBase = Feature(geometry=Point((longtitude, lattitude)))
		base_locations.append(milBase)
	return base_locations

datasource_BND = open_shapefile("milBase_BND.shp")
datasource_PT = open_shapefile("milBase_PT.shp")


# Base Location
base_locations_PT = get_base_location(datasource_PT)
print(base_locations_PT)


