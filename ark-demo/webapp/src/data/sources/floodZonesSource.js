import { MAP_TYPES } from '@deck.gl/carto';

const FLOOD_ZONES_SOURCE_ID = 'floodZonesSource';

const source = {
  id: FLOOD_ZONES_SOURCE_ID,
  type: MAP_TYPES.TILESET,
  connection: 'geo-solution-demos',
  data: `geo-solution-demos.nfhl.S_FLD_HAZ_AR_tileset`,
};

export default source;
