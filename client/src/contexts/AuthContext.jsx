import { createContext, useState, useContext } from "react";
import axios from "axios";

const AuthContext = createContext();

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const AuthProvider = ({ children }) => {
  const [authState, setAuthState] = useState({
    isAuthenticated: false,
    user: null,
  });

  const login = async (email, contraseña) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/login/`, {
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
