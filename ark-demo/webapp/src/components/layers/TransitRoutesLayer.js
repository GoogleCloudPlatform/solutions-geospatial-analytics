import { useSelector } from 'react-redux';
import { CartoLayer } from '@deck.gl/carto';
import { selectSourceById } from '@carto/react-redux';
import { useCartoLayerProps } from '@carto/react-api';
import htmlForFeature from 'utils/htmlForFeature';

export const TRANSIT_ROUTES_LAYER_ID = 'transitRoutesLayer';

export default function TransitRoutesLayer() {
  const { transitRoutesLayer } = useSelector((state) => state.carto.layers);
  const source = useSelector((state) => selectSourceById(state, transitRoutesLayer?.source));
  const cartoLayerProps = useCartoLayerProps({ source });

  if (transitRoutesLayer && source) {
    return new CartoLayer({
      ...cartoLayerProps,
      id: TRANSIT_ROUTES_LAYER_ID,
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
