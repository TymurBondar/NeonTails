import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, RouterProvider, createBrowserRouter } from 'react-router-dom';
import './index.css';
import Root from './routes/Root';


const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
);
