import { Link } from "react-router-dom";
import logo from "../assets/Logo.png";
import { useAuth } from "../contexts/AuthContext";

export default function Navbar() {
  const { authState, logout } = useAuth();
  return (
    <div className="navbar bg-base-100">
      <div className="navbar-start">
        <div className="dropdown">
          <div tabIndex={0} role="button" className="btn btn-ghost lg:hidden">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M4 6h16M4 12h8m-8 6h16"
              />
            </svg>
          </div>
          <ul
            tabIndex={0}
            className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
          >
          </ul>
        </div>
        <Link className="btn btn-ghost text-xl">
          <img src={logo} alt="Logo" className="h-8 mr-2" />
          Partenón
        </Link>
      </div>
      <div className="navbar-center hidden lg:flex">
        <ul className="menu menu-horizontal px-1">
        </ul>
      </div>
      <div className="navbar-end">
        {authState.isAuthenticated ? 
          <div>
            <Link to={'/protected/books'} className="btn btn-ghost">Mis Libros</Link>
            <Link to={'/'} onClick={logout} className="btn btn-ghost">Cerrar sesión</Link>
          </div> : (
          <Link to={"/login"} className="btn btn-ghost">
            Login
          </Link>
        )}
      </div>
    </div>
  );
}
