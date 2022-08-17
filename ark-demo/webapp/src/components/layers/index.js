import FloodZonesLayer from './FloodZonesLayer';
import BuildingsLayer from './BuildingsLayer';
// [hygen] Import layers

export const getLayers = () => {
  return [
    FloodZonesLayer(),
    BuildingsLayer(),
    // [hygen] Add layer
  ];
};
