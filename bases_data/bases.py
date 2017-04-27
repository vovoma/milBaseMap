import ogr #load ogr libraries

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

def 


datasource_BND = open_shapefile("milBase_BND.shp")
datasource_PT = open_shapefile("milBase_PT.shp")
