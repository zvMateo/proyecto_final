import React from 'react';
import backgroundImage from '../assets/henry-be-lc7xcWebECc-unsplash.jpg'; // Ajusta esta ruta según la estructura de tu proyecto


export default function Home() {
  return (
    <div
      className="container mx-auto p-4"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        minHeight: '100vh',
        color: '#f0f0f0', // Color claro para el texto
      }}
    >
       {/* Main Content */}
      <div className="flex flex-col items-center justify-center h-full bg-black bg-opacity-50 text-center">
        <h1 className="text-4xl md:text-6xl font-bold mb-4">La educación es el futuro</h1>
        <p className="text-lg md:text-xl mb-6">Descubre cómo podemos ayudarte a alcanzar tus metas</p>
        <button className="btn btn-primary">Más información</button>
      </div>
      {/* <div className="hero bg-opacity-75 bg-black text-center py-10">
        <div className="hero-content">
          <div>
            <h1 className="text-5xl font-bold" style={{ color: '#A6A6A6' }}>¡Bienvenidos a la Librería Virtual!</h1>
            <p className="py-6" style={{ color: '#F2F2F2' }}>Explora nuestra colección de libros y encuentra tus próximos favoritos.</p>
            <button className="btn btn-primary" style={{ backgroundColor: '#262626', borderColor: '#483d8b' }}>Explorar Libros</button>
          </div>
        </div>
      </div> */}

      {/* <div className="mt-10 bg-opacity-75 bg-black p-4 rounded">
        <h2 className="text-3xl font-semibold" style={{ color: '#fafad2' }}>Libros Destacados</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
          {/* Aquí puedes mapear una lista de libros destacados */}
          {/* <div className="card shadow-lg" style={{ backgroundColor: 'rgba(0, 0, 0, 0.6)' }}>
            <div className="card-body">
              <h3 className="card-title" style={{ color: '#fafad2' }}>Título del Libro 1</h3>
              <p style={{ color: '#dcdcdc' }}>Descripción breve del libro.</p>
              <button className="btn btn-primary" style={{ backgroundColor: '#483d8b', borderColor: '#483d8b' }}>Ver Más</button>
            </div>
          </div>
          {/* Repite la estructura del libro para otros libros destacados */}
        {/* </div>
      </div> */} 
    </div>
  );
}


// export default function Home() {
//   const backgroundImage = "url('/assets/fondo-home.jpg')"; // Asegúrate de que esta ruta sea correcta y accesible

//   return (
//     <div
//       className="container mx-auto p-4"
//       style={{
//         backgroundImage: backgroundImage,
//         backgroundSize: 'cover',
//         backgroundPosition: 'center',
//         minHeight: '100vh',
//         color: 'white',
//       }}
//     >
//       <div className="hero bg-opacity-75 bg-black text-center py-10">
//         <div className="hero-content">
//           <div>
//             <h1 className="text-5xl font-bold">¡Bienvenidos a la Librería Virtual!</h1>
//             <p className="py-6">Explora nuestra colección de libros y encuentra tus próximos favoritos.</p>
//             <button className="btn btn-primary">Explorar Libros</button>
//           </div>
//         </div>
//       </div>

//       <div className="mt-10 bg-opacity-75 bg-black p-4 rounded">
//         <h2 className="text-3xl font-semibold">Libros Destacados</h2>
//         <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
//           {/* Aquí puedes mapear una lista de libros destacados */}
//           <div className="card shadow-lg">
//             <div className="card-body">
//               <h3 className="card-title">Título del Libro 1</h3>
//               <p>Descripción breve del libro.</p>
//               <button className="btn btn-primary">Ver Más</button>
//             </div>
//           </div>
//           {/* Repite la estructura del libro para otros libros destacados */}
//         </div>
//       </div>
//     </div>
//   );
// }



