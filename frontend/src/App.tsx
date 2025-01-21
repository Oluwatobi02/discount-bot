import DashboardIcon from '@mui/icons-material/Dashboard';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import BarChartIcon from '@mui/icons-material/BarChart';
import DescriptionIcon from '@mui/icons-material/Description';
import LayersIcon from '@mui/icons-material/Layers';
import { ReactRouterAppProvider } from '@toolpad/core/react-router';
import { Outlet } from 'react-router';
import { Navigation } from '@toolpad/core/AppProvider';
import Navbar from './components/navbar/Navbar';
import LogoNoBackground from './assets/logo-no-background';
function App() {
  const NAVIGATION: Navigation = [
    {
      kind: 'header',
      title: 'Menu',
    },
    {
      segment: 'home',
      title: 'Home',
      icon: <DashboardIcon />,
    },
    {
      segment: 'orders',
      title: 'Orders',
      icon: <ShoppingCartIcon />,
    },
    {
      kind: 'divider',
    },
    {
      kind: 'header',
      title: 'Analytics',
    },
    {
      segment: 'reports',
      title: 'Reports',
      icon: <BarChartIcon />,
      children: [
        {
          segment: 'sales',
          title: 'Sales',
          icon: <DescriptionIcon />,
        },
        {
          segment: 'traffic',
          title: 'Traffic',
          icon: <DescriptionIcon />,
        },
      ],
    },
    {
      segment: 'watchlist',
      title: 'Watchlist',
      icon: <LayersIcon />,
    },
  ];
  const BRANDING = {
    title: 'Deal Spree',
    logo: <LogoNoBackground />,
    homeUrl: '/',
  }
  return (
    <>
      <ReactRouterAppProvider navigation={NAVIGATION} branding={BRANDING}>
        <Navbar />
        <Outlet />
      </ReactRouterAppProvider>
    </>
  )
}

export default App
