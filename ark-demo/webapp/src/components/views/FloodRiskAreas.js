import { useEffect } from 'react';
import floodZonesSource from 'data/sources/floodZonesSource';
import { FLOOD_ZONES_LAYER_ID } from 'components/layers/FloodZonesLayer';
import { useDispatch } from 'react-redux';
import {
  addLayer,
  removeLayer,
  addSource,
  removeSource,
} from '@carto/react-redux';

import { makeStyles } from '@material-ui/core/styles';
import { Grid } from '@material-ui/core';

const useStyles = makeStyles(() => ({
  floodRiskAreas: {},
}));

export default function FloodRiskAreas() {
  const dispatch = useDispatch();
  const classes = useStyles();

  useEffect(() => {
    dispatch(addSource(floodZonesSource));

    dispatch(
      addLayer({
        id: FLOOD_ZONES_LAYER_ID,
        source: floodZonesSource.id,
      }),
    );

    return () => {
      dispatch(removeLayer(FLOOD_ZONES_LAYER_ID));
      dispatch(removeSource(floodZonesSource.id));
    };
  }, [dispatch]);

  // [hygen] Add useEffect

  return (
    <Grid container direction='column' className={classes.floodRiskAreas}>
      <Grid item>Hello World</Grid>
    </Grid>
  );
}
