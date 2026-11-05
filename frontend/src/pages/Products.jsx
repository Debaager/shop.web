import { useEffect, useState } from 'react';
import api from '../api';

export default function Products() {
  const [items, setItems] = useState([]);
  const [sort, setSort] = useState('name');
  const [category, setCategory] = useState('');

  useEffect(() => {
    api.get('/products/', { params: { sort, category } })
       .then(r => setItems(r.data));
  }, [sort, category]);

  const add = id => api.post(/cart//).then(() => alert('Добавлено в корзину'));

  return (
    <div>
      <h2>Товары</h2>
      <div className="d-flex mb-3">
        <select className="form-select me-2" value={sort} onChange={e => setSort(e.target.value)} style={{width: '200px'}}>
          <option value="name">Имя ↑</option>
          <option value="-name">Имя ↓</option>
          <option value="price">Цена ↑</option>
          <option value="-price">Цена ↓</option>
        </select>
        <input className="form-control" placeholder="Категория" value={category} onChange={e => setCategory(e.target.value)} style={{width: '200px'}} />
      </div>
      <div className="row">
        {items.map(p => (
          <div key={p.id} className="col-md-4 mb-3">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{p.name}</h5>
                <p className="text-muted">{p.category}</p>
                <p className="fw-bold">{p.price} ₽</p>
                <button className="btn btn-primary" onClick={() => add(p.id)}>В корзину</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
