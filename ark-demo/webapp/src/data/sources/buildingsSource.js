import { MAP_TYPES } from '@deck.gl/carto';

const BUILDINGS_SOURCE_ID = 'buildingsSource';

const source = {
  id: BUILDINGS_SOURCE_ID,
  type: MAP_TYPES.TILESET,
  connection: 'geo-solution-demos',
  data: `geo-solution-demos.other.OSM_buildings_tileset`,
};

export default source;
