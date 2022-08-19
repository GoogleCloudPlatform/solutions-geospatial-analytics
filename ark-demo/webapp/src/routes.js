import { lazy } from 'react';
import ProtectedRoute from 'components/common/ProtectedRoute';
import DefaultView from 'components/common/DefaultView';

const Main = lazy(() => import(/* webpackPrefetch: true */ 'components/views/main/Main'));
const NotFound = lazy(() => import('components/views/NotFound'));
const Login = lazy(() => import('components/views/Login'));
const FloodRiskAreas = lazy(() => import('components/views/FloodRiskAreas.js'));
const BuildingRisk = lazy(() => import('components/views/BuildingRisk.js'));
const TransitRoutes = lazy(() => import('components/views/TransitRoutes.js'));
// [hygen] Import views

export const ROUTE_PATHS = {
  LOGIN: '/login',
  DEFAULT: '/',
  NOT_FOUND: '/404',
  FLOOD_RISK_AREAS: '/floodrisk',
  BUILDING_RISK: '/buildings',
  TRANSIT_ROUTES: '/transit',
  // [hygen] Add path routes
};

const routes = [
  {
    path: ROUTE_PATHS.DEFAULT,
    element: (
      <ProtectedRoute>
        <DefaultView>
          <Main />
        </DefaultView>
      </ProtectedRoute>
    ),
    children: [
      // { path: '/', element: <Navigate to='/<your default view>' /> },
      { path: ROUTE_PATHS.FLOOD_RISK_AREAS, element: <FloodRiskAreas /> },
      { path: ROUTE_PATHS.BUILDING_RISK, element: <BuildingRisk /> },
      { path: ROUTE_PATHS.TRANSIT_ROUTES, element: <TransitRoutes /> },
      // [hygen] Add routes
    ],
  },
  { path: ROUTE_PATHS.LOGIN, element: <Login /> },
  {
    path: '*',
    element: (
      <DefaultView>
        <NotFound />
      </DefaultView>
    ),
  },
];

export default routes;
