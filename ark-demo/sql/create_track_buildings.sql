CREATE TABLE
  `geo-solution-demos.ark_demo.ian_buildings_zone_a`
CLUSTER BY
  geom AS (
  SELECT
    FLD_ZONE,
    building.geometry AS geom
  FROM
    `geo-solution-demos.ark_demo.osm_buildings` AS building
  INNER JOIN
    `geo-solution-demos.nfhl.S_FLD_HAZ_AR` AS floodzone
  ON
    (ST_INTERSECTS(building.geometry, floodzone.geom))
  INNER JOIN
    `geo-solution-demos.nhc.nhc_5day_pgn` cone
  ON
    (ST_INTERSECTS(building.geometry, cone.geom))
  WHERE
    STARTS_WITH(floodzone.FLD_ZONE, 'A') )
