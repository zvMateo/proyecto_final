import { useState, useEffect } from "react";
import {
  getAllBooksByUser,
  updateBook,
  deleteBook,
  addBook,
} from "../utils/requests"; // Asegúrate de importar addBook
import { useAuth } from "../contexts/AuthContext";

export default function Books() {
  const [books, setBooks] = useState([]);
  const [selectedBook, setSelectedBook] = useState(null);
  const [newBook, setNewBook] = useState({ nombre: "", descripcion: "" });
  const [showEditModal, setShowEditModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [showAddModal, setShowAddModal] = useState(false);
  const [page, setPage] = useState(1);
  const limit = 10;
  const { authState } = useAuth();

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const books = await getAllBooksByUser(authState.user.id, page, limit);
        setBooks(books);
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    };

    fetchBooks();
  }, [authState.user.id, page]);

  const handlePreviousPage = () => {
    if (page > 1) setPage(page - 1);
  };

  const handleNextPage = () => {
    setPage(page + 1);
  };

  const handleEdit = (book) => {
    setSelectedBook(book);
    setShowEditModal(true);
  };

  const handleDelete = (book) => {
    setSelectedBook(book);
    setShowDeleteModal(true);
  };

  const handleSaveChanges = async () => {
    try {
      await updateBook(selectedBook);
      setBooks(
        books.map((book) => (book.id === selectedBook.id ? selectedBook : book))
      );
      setShowEditModal(false);
    } catch (error) {
      console.error("Error updating book:", error);
    }
  };

  const handleConfirmDelete = async () => {
    try {
      await deleteBook(selectedBook.id);
      setBooks(books.filter((book) => book.id !== selectedBook.id));
      setShowDeleteModal(false);
    } catch (error) {
      console.error("Error deleting book:", error);
    }
  };

  const handleAddBook = async () => {
    try {
      const addedBook = await addBook(authState.user.id, newBook);
      setBooks([...books, addedBook]);
      setNewBook({ nombre: "", descripcion: "" });
      setShowAddModal(false);
    } catch (error) {
      console.error("Error adding book:", error);
    }
  };

  return (
    <section className="pt-20 pb-10 flex-1 w-full flex flex-col justify-center items-center overflow-hidden">
    <div className="w-full px-4 md:px-20 flex-1 overflow-auto mt-4">
      <button className="btn btn-primary mb-4" onClick={() => setShowAddModal(true)}>Agregar Libro</button>
  
      <table className="table table-zebra w-full">
        <thead>
          <tr>
            <th></th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {books.length > 0 ? (
            books.map((book, index) => (
              <tr key={book.id}>
                <th>{index + 1 + (page - 1) * limit}</th>
                <td>{book.nombre}</td>
                <td>{book.descripcion}</td>
                <td>
                  <button className="btn btn-primary" onClick={() => handleEdit(book)}>Editar</button>
                  <button className="btn btn-error" onClick={() => handleDelete(book)}>Eliminar</button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No hay libros disponibles.</td>
            </tr>
          )}
        </tbody>
      </table>
      <div className="join w-full flex justify-center items-center mt-4">
        <button className="join-item btn" onClick={handlePreviousPage} disabled={page === 1}>
          «
        </button>
        <button className="join-item btn">Página {page}</button>
        <button className="join-item btn" onClick={handleNextPage}>
          »
        </button>
      </div>
    </div>
  
    {/* Modal para editar libro */}
    {showEditModal && selectedBook && (
      <div className="modal modal-open">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Editar Libro</h3>
          <div className="py-4">
            <input 
              type="text" 
              value={selectedBook.nombre} 
              onChange={(e) => setSelectedBook({ ...selectedBook, nombre: e.target.value })} 
              className="input input-bordered w-full mb-4"
            />
            <textarea 
              value={selectedBook.descripcion} 
              onChange={(e) => setSelectedBook({ ...selectedBook, descripcion: e.target.value })} 
              className="textarea textarea-bordered w-full"
            />
          </div>
          <div className="modal-action">
            <button className="btn btn-primary" onClick={handleSaveChanges}>Guardar</button>
            <button className="btn" onClick={() => setShowEditModal(false)}>Cancelar</button>
          </div>
        </div>
      </div>
    )}
  
    {/* Modal para confirmar eliminación */}
    {showDeleteModal && selectedBook && (
      <div className="modal modal-open">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Confirmar Eliminación</h3>
          <p>¿Estás seguro de que deseas eliminar este libro?</p>
          <div className="modal-action">
            <button className="btn btn-error" onClick={handleConfirmDelete}>Eliminar</button>
            <button className="btn" onClick={() => setShowDeleteModal(false)}>Cancelar</button>
          </div>
        </div>
      </div>
    )}
  
    {/* Modal para agregar libro */}
    {showAddModal && (
      <div className="modal modal-open">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Agregar Libro</h3>
          <div className="py-4">
            <input 
              type="text" 
              value={newBook.nombre} 
              onChange={(e) => setNewBook({ ...newBook, nombre: e.target.value })} 
              className="input input-bordered w-full mb-4"
              placeholder="Nombre del libro"
            />
            <textarea 
              value={newBook.descripcion} 
              onChange={(e) => setNewBook({ ...newBook, descripcion: e.target.value })} 
              className="textarea textarea-bordered w-full"
              placeholder="Descripción del libro"
            />
          </div>
          <div className="modal-action">
            <button className="btn btn-primary" onClick={handleAddBook}>Agregar</button>
            <button className="btn" onClick={() => setShowAddModal(false)}>Cancelar</button>
          </div>
        </div>
      </div>
    )}
  </section>
  
  );
}
