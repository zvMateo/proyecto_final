import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from './App.jsx';
import ProtectedRoutes from './utils/ProtectedRoutes.jsx';
import './index.css';
import Login from './pages/Login.jsx';
import Home from './pages/Home.jsx';
import Books from './pages/Books.jsx';
import { AuthProvider } from './contexts/AuthContext.jsx';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,  // Navbar visible
    children: [
      {
        path: "/",
        element: <Home />  // Componente de la página principal
      },
      {
        path: "/protected",
        element: <ProtectedRoutes />,
        children: [
          {
            path: "books",
            element: <Books />  // Nueva ruta protegida
          }
        ]  // Usa este para más rutas protegidas
      }
    ]
  },
  {
    path: "/login",
    element: <Login />  // Navbar no visible
  }
]);


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    
    <AuthProvider>
    <RouterProvider router={router} />
    </AuthProvider>
  
  </React.StrictMode>,
)
