import FloodZonesLayer from './FloodZonesLayer';
import BuildingsLayer from './BuildingsLayer';
import TransitRoutesLayer from './TransitRoutesLayer';
// [hygen] Import layers

export const getLayers = () => {
  return [
    FloodZonesLayer(),
    BuildingsLayer(),
    TransitRoutesLayer(),
    // [hygen] Add layer
  ];
};
