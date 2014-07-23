import os
import arcpy    
from arcpy import env
env.workspace = "P:/Python/Data/Exercise07"
fc = r"P:/Python/Data/Exercise07/airports.shp"
cursor = arcpy.da.SearchCursor(fc, "", '"FEATURE", = Airport')
arcpy.Buffer_analysis(cursor, r"P:/Python/Data/Exercise07/airports.shp", "15000 meters")
  
from arcpy import env
env.workspace = "P:/Python/Data/Exercise07"
fc = r"P:/Python/Data/Exercise07/airports.shp"
cursor = arcpy.da.SearchCursor(fc, "", '"FEATURE", = Seaplane Base')
arcpy.Buffer_analysis(cursor, r"P:/Python/Data/Exercise07/airports.shp", "7500 meters")

from arcpy import env
env.workspace = "P:/Python/Data/Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 20)
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1]= "NO"
    cursor.updateRow(row)
