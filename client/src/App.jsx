import React from "react";
import { Outlet } from "react-router-dom";
import Navbar from "./components/Navbar"; 



const App = () => {
  return (
    <>
      <header className="absolute w-full p-4 z-10">
        <Navbar />
      </header>
      <section
        className="min-h-screen w-full flex flex-col justify-center items-center bg-transparent"
      >
        <Outlet />
        
      </section>
    </>
  );
};

export default App;
