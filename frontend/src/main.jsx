import React from 'react';
import ReactDOM from 'react-dom/client';
import {RouterProvider, createBrowserRouter } from 'react-router-dom';
import './index.css';
import Root from './routes/Root';
import Artists from './routes/Artists';
import Exhibitions from './routes/Exhibitions';
import ThemedExhibition from './routes/ThemedExhibition';
import Home from './routes/Home';
import ArtistPage from './routes/ArtistPage';
import Signin from './routes/Signin';
import NotFound from './routes/NotFound';


const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    children:[
      {
        path: '/',
        element: <Home/>,
      },
      {
        path: '/artists',
        element: <Artists/>,
      },
      {
        path: '/artists/:id',
        element: <ArtistPage/>,
      },
      {
        path: '/exhibitions',
        element: <Exhibitions/>
      },
      {
        path: '/exhibitions/:theme',
        element: <ThemedExhibition/>
      },
      {
        path: '/signin',
        element: <Signin/>
      },
      {
        path: '*',
        element: <NotFound/>
      },
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
);
