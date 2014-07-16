import os
import arcpy    

arcpy.env.workspace = "P:/Python/Data/Exercise06"
outWorkspace = "P:/Python/ch6.gdb"
fclist = arcpy.ListFeatureClasses("")

for feature in fclist:
    desc = arcpy.Describe(feature)
    print("{} is a {}".format(desc.name, desc.shapeType))
    if desc.shapeType == 'Polygon':
        print('it is a polygon')
        outFeatureClass = os.path.join(outWorkspace, feature.strip(".shp"))
        arcpy.CopyFeatures_management(feature, outFeatureClass)

