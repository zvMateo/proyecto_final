import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

// Obtener todos los libros de un usuario
export const getAllBooksByUser = async (userId, page = 1, limit = 10) => {
  const skip = (page - 1) * limit;
  const response = await axios.get(
    `${API_BASE_URL}/users/${userId}/libros?skip=${skip}&limit=${limit}`
  );
  return response.data;
};

// Actualizar un libro
export const updateBook = async (book) => {
  try {
    const response = await axios.put(`${API_BASE_URL}/libros/${book.id}`, book);
    return response.data;
  } catch (error) {
    console.error("Error updating book:", error);
    throw error;
  }
};

// Eliminar un libro
export const deleteBook = async (bookId) => {
  const response = await axios.delete(`${API_BASE_URL}/libros/${bookId}`);
  return response.data;
};

// Nueva función para agregar un libro
export const addBook = async (userId, book) => {
  const response = await axios.post(`${API_BASE_URL}/libros/`, { ...book, propietario_id: userId });
  return response.data;
};


// export const addBook = async (userId, book) => {
//   const response = await axios.post(`${API_BASE_URL}/libros`, book, {
//     params: {
//       propietario_id: userId
//     }
//   });
//   return response.data;
// };

// export const addBook = async (userId, book) => {
//   const response = await axios.post(`${API_BASE_URL}/libros?propietario_id=${userId}`, book);
//   return response.data;
// };

// import axios from "axios";

// export const getAllBooksByUser = async (userId, page = 1, limit = 10) => {
//   const skip = (page - 1) * limit;
//   const response = await axios.get(
//     `http://127.0.0.1:8000/api/users/${userId}/libros?skip=${skip}&limit=${limit}`
//   );
//   return response.data;
// };

