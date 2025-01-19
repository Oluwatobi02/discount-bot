import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router';
import './index.css'
import App from './App.tsx'
import { Provider } from "@/components/ui/provider"
import Layout from './pages/Layout.tsx';
import Home from './pages/Home.tsx';
import SigninPage from './pages/(auth)/Signin.tsx';
import SignupPage from './pages/(auth)/Signup.tsx';
export const router = createBrowserRouter([
  {
    Component: App, // root layout route
    children: [
      {
        path: '/',
        Component: Layout,
        children: [
          {
            path: '/home',
            Component: Home,
          },
          ]
      },
      {
        path: '/sign-in',
        Component: SigninPage,
      },
      {
        path: '/sign-up',
        Component: SignupPage,
      },
      
    ],
  },
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Provider>
    {/* <App /> */}
    <RouterProvider router={router} />
    </Provider>
  </StrictMode>
)
