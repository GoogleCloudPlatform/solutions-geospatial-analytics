import { useSelector } from 'react-redux';
import { CartoLayer } from '@deck.gl/carto';
import { selectSourceById } from '@carto/react-redux';
import { useCartoLayerProps } from '@carto/react-api';
import htmlForFeature from 'utils/htmlForFeature';

export const FLOOD_ZONES_LAYER_ID = 'floodZonesLayer';

export default function FloodZonesLayer() {
  const { floodZonesLayer } = useSelector((state) => state.carto.layers);
  const source = useSelector((state) => selectSourceById(state, floodZonesLayer?.source));
  const cartoLayerProps = useCartoLayerProps({ source });

  if (floodZonesLayer && source) {
    return new CartoLayer({
      ...cartoLayerProps,
      id: FLOOD_ZONES_LAYER_ID,
      getFillColor: [241, 109, 122],
      pointRadiusMinPixels: 2,
      getLineColor: [255, 0, 0],
      lineWidthMinPixels: 1,
      pickable: true,
      onHover: (info) => {
        if (info?.object) {
          info.object = {
            html: htmlForFeature({ feature: info.object }),
            style: {},
          };
        }
      },
    });
  }
}
