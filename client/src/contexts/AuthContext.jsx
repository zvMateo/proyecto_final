// src/contexts/AuthContext.jsx
import { createContext, useState, useContext } from "react";
import axios from "axios";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    isAuthenticated: false,
    user: null,
  });

  const login = async (email, contraseña) => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/login/", {
        email,
        contraseña,
      });
      setAuthState({
        isAuthenticated: true,
        user: response.data,
      });
    } catch (error) {
      console.error(
        "Login failed",
        error.response ? error.response.data : error.message
      );
      throw new Error(
        error.response?.data?.detail || "Error al iniciar sesión"
      );
    }
  };

  const logout = () => {
    setAuthState({
      isAuthenticated: false,
      user: null,
    });
  };

  return (
    <AuthContext.Provider value={{ authState, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
