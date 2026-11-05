import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Products from './pages/Products';
import Cart from './pages/Cart';

export default function App() {
  return (
    <BrowserRouter>
      <nav className="navbar navbar-dark bg-dark p-3 mb-4">
        <div className="container">
          <Link to="/" className="navbar-brand">SPA Магазин</Link>
          <div>
            <Link to="/" className="btn btn-outline-light me-2">Товары</Link>
            <Link to="/cart" className="btn btn-outline-light">Корзина</Link>
          </div>
        </div>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/" element={<Products />} />
          <Route path="/cart" element={<Cart />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
