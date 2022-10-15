# nhc_forecast

Load NHC hurricane forecast cones into BigQuery for analysis

## Make tables

```
bq mk nhc.nhc_5day_pgn nhc_5day_pgn.json
bq mk nhc.nhc_5day_pts nhc_5day_pts.json
bq mk nhc.nhc_5day_lin nhc_5day_lin.json
```


