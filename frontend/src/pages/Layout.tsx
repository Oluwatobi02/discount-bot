import DashboardIcon from '@mui/icons-material/Dashboard';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import BarChartIcon from '@mui/icons-material/BarChart';
import DescriptionIcon from '@mui/icons-material/Description';
import LayersIcon from '@mui/icons-material/Layers';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { useDemoRouter } from '@toolpad/core/internal';
import { createTheme } from '@mui/material/styles';

interface DemoProps {

    window?: () => Window;
    children: React.ReactNode;
  }
  

  const demoTheme = createTheme({
    cssVariables: {
      colorSchemeSelector: 'data-toolpad-color-scheme',
    },
    colorSchemes: { light: true, dark: true },
    breakpoints: {
      values: {
        xs: 0,
        sm: 600,
        md: 600,
        lg: 1200,
        xl: 1536,
      },
    },
  });
export default function Layout(props: DemoProps) {
    const { window } = props;
  
    const router = useDemoRouter('/dashboard');
    const NAVIGATION: Navigation = [
        {
          kind: 'header',
          title: 'Main items',
        },
        {
          segment: 'dashboard',
          title: 'Dashboard',
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
    // Remove this const when copying and pasting into your project.
    const demoWindow = window !== undefined ? window() : undefined;
    return (
      // preview-start
      <AppProvider
        navigation={NAVIGATION}
        router={router}
        theme={demoTheme}
        window={demoWindow}
        branding={{
          // logo: <img src="https://mui.com/static/logo.png" alt="MUI logo" />,
          title: 'Price Tracker',
          homeUrl: '/',
        }}
      >
        <DashboardLayout>
          {props.children}
        </DashboardLayout>
      </AppProvider>
      // preview-end
    );
  }