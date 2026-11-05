import { useEffect, useState } from 'react';
import api from '../api';

export default function Cart() {
  const [data, setData] = useState({ items: [], total: 0 });

  const load = () => api.get('/cart/').then(r => setData(r.data));
  useEffect(() => { load(); }, []);

  const remove = id => api.delete(/cart//).then(load);

  return (
    <div>
      <h2>Корзина</h2>
      <table className="table mt-3 bg-white">
        <thead><tr><th>Товар</th><th>Цена</th><th>Кол-во</th><th>Сумма</th><th></th></tr></thead>
        <tbody>
        {data.items.map(i => (
          <tr key={i.id}>
            <td>{i.name}</td>
            <td>{i.price} ₽</td>
            <td>{i.quantity}</td>
            <td>{i.subtotal} ₽</td>
            <td><button className="btn btn-danger btn-sm" onClick={() => remove(i.id)}>Удалить</button></td>
          </tr>
        ))}
        </tbody>
      </table>
      <h4>Итого: {data.total} ₽</h4>
      <button className="btn btn-success" disabled={!data.items.length}>Оформить покупку</button>
    </div>
  );
}
