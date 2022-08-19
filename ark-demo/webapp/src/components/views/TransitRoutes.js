import { useEffect } from 'react';
import transitRoutesSource from 'data/sources/transitRoutesSource';
import { TRANSIT_ROUTES_LAYER_ID } from 'components/layers/TransitRoutesLayer';
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
  transitRoutes: {},
}));

export default function TransitRoutes() {
  const dispatch = useDispatch();
  const classes = useStyles();

  useEffect(() => {
    dispatch(addSource(transitRoutesSource));

    dispatch(
      addLayer({
        id: TRANSIT_ROUTES_LAYER_ID,
        source: transitRoutesSource.id,
      }),
    );

    return () => {
      dispatch(removeLayer(TRANSIT_ROUTES_LAYER_ID));
      dispatch(removeSource(transitRoutesSource.id));
    };
  }, [dispatch]);

  // [hygen] Add useEffect

  return (
    <Grid container direction='column' className={classes.transitRoutes}>
      <Grid item>Hello World</Grid>
    </Grid>
  );
}
