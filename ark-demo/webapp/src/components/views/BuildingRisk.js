import { useEffect } from 'react';
import buildingsSource from 'data/sources/buildingsSource';
import { BUILDINGS_LAYER_ID } from 'components/layers/BuildingsLayer';
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
  buildingRisk: {},
}));

export default function BuildingRisk() {
  const dispatch = useDispatch();
  const classes = useStyles();

  useEffect(() => {
    dispatch(addSource(buildingsSource));

    dispatch(
      addLayer({
        id: BUILDINGS_LAYER_ID,
        source: buildingsSource.id,
      }),
    );

    return () => {
      dispatch(removeLayer(BUILDINGS_LAYER_ID));
      dispatch(removeSource(buildingsSource.id));
    };
  }, [dispatch]);

  // [hygen] Add useEffect

  return (
    <Grid container direction='column' className={classes.buildingRisk}>
      <Grid item>Hello World</Grid>
    </Grid>
  );
}
