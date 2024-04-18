import io
import geopandas as gpd
import fiona
from fiona.io import ZipMemoryFile
from fiona.transform import transform_geom

filename = 'NFHL_02_20211104.zip'
zipgdb = io.BytesIO(open(filename, 'rb').read())

#layers = fiona.listlayers(ZipMemoryFile(zipgdb, ext='.gdb.zip'))
#print(layers)

with (ZipMemoryFile(zipgdb, ext='.gdb.zip')) as memfile:
    layers = memfile.listlayers()
    for layer in layers:
        with memfile.open(layer=layer) as src:
            gdf = gpd.GeoDataFrame.from_features(src, crs=src.crs)
            gdf.to_crs('epsg:4326')
            #gdf.to_parquet('{}.parquet'.format(layer))
