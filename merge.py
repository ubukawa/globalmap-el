from osgeo import gdal
import glob

demList = glob.glob("src/gm_el_[01-04]_[01-12].tif")
print(demList)
