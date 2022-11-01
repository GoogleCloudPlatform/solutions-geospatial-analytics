CREATE TABLE
  ark_demo.osm_buildings
CLUSTER BY
  geometry AS (
  SELECT
    geometry
  FROM
    `bigquery-public-data.geo_openstreetmap.planet_layers`,
    UNNEST(all_tags) AS tags
  WHERE
    tags.key = "building"
    AND st_geometrytype(geometry) = "ST_Polygon" )
