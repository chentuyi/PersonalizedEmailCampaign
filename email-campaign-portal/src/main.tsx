import React from 'react'
import ReactDOM from 'react-dom/client'
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Root from './pages/Root.js';
import Home from './pages/Home.tsx';
import Portal from './pages/Portal.js';
import Product from './pages/Product.js';
import './index.css'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    children: [
      { path: 'home', element: <Home /> },
      { path: 'portal', element: <Portal /> },
      { path: 'product', element: <Product /> },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
