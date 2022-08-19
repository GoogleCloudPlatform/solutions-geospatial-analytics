import { MAP_TYPES } from '@deck.gl/carto';

const TRANSIT_ROUTES_SOURCE_ID = 'transitRoutesSource';

const source = {
  id: TRANSIT_ROUTES_SOURCE_ID,
  type: MAP_TYPES.TABLE,
  connection: 'geo-solution-demos',
  data: `TODO`,
};

export default source;
