import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, RouterProvider, createBrowserRouter } from 'react-router-dom';
import './index.css';
import Root from './routes/Root';
import Artists from './routes/Artists';
import Exhibitions from './routes/Exhibitions';


const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    children:[
      {
        path: '/',
        element: <>Welcome to the homepage!</>,
      },
      {
        path: '/artists',
        element: <Artists/>
      },
      {
        path: '/exhibitions',
        element: <Exhibitions/>
      },
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
);
