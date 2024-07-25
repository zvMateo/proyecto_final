import { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";

export default function LoginForm() {
  const { login, authState } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
      navigate("/");
    } catch (error) {
      setError(error.message);
      setTimeout(() => {
        setError("");
      }, 5000);
    }
  };

  return (
    <section className="h-screen w-full flex justify-center items-center">
      {error.length > 0 ? (
        <div className="absolute top-20">
          <div role="alert" className="alert alert-error">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6 shrink-0 stroke-current"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <span>Oops! {error}</span>
          </div>
        </div>
      ) : null}
      <form className="card bg-base-200 w-80" onSubmit={handleSubmit}>
        <div className="card-body">
          <input
            type="email"
            placeholder="Email"
            className="input input-bordered"
            value={email}
            onChange={handleEmailChange}
            required
            autoComplete="true"
          />
          <input
            type="password"
            placeholder="Contraseña"
            className="input input-bordered"
            value={password}
            onChange={handlePasswordChange}
            required
            autoComplete="true"
          />
          <button type="submit" className="btn btn-neutral">
            Iniciar Sesión
          </button>
        </div>
      </form>
    </section>
  );
}
