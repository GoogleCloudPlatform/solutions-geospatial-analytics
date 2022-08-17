import { useSelector } from 'react-redux';
import { CartoLayer } from '@deck.gl/carto';
import { selectSourceById } from '@carto/react-redux';
import { useCartoLayerProps } from '@carto/react-api';
import htmlForFeature from 'utils/htmlForFeature';

export const BUILDINGS_LAYER_ID = 'buildingsLayer';

export default function BuildingsLayer() {
  const { buildingsLayer } = useSelector((state) => state.carto.layers);
  const source = useSelector((state) => selectSourceById(state, buildingsLayer?.source));
  const cartoLayerProps = useCartoLayerProps({ source });

  if (buildingsLayer && source) {
    return new CartoLayer({
      ...cartoLayerProps,
      id: BUILDINGS_LAYER_ID,
      getFillColor: [241, 109, 122],
      pointRadiusMinPixels: 2,
      getLineColor: [255, 0, 0],
      lineWidthMinPixels: 1,
      pickable: true,
      zoom: 12,
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
