#coding=utf-8
import bases 

datasource_BND = bases.open_shapefile("bases_data/milBase_BND.shp")
datasource_PT = bases.open_shapefile("bases_data/milBase_PT.shp")
base_locations_PT = bases.get_base_location(datasource_PT)
baseList = bases.FeatureCollection(base_locations_PT)

print(baseList)
def main():
	print(baseList)

if __name__ == "__main__":
	main()