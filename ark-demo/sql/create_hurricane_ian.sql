CREATE TABLE
  ark_demo.hurricanes_2022 AS (
  SELECT
    *,
    ST_GEOGPOINT(longitude, latitude) AS geom
  FROM
    `bigquery-public-data.noaa_hurricanes.hurricanes`
  WHERE
    name = "IAN"
    AND iso_time > "2022-05-01")
