
import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function IPOList() {
  const [ipos, setIpos] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/ipos/')
      .then(res => setIpos(res.data));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Upcoming IPO</h2>
      <div className="grid grid-cols-3 gap-4">
        {ipos.map(ipo => (
          <div key={ipo.id} className="border p-4 rounded shadow">
            <h3 className="text-lg font-semibold">{ipo.company}</h3>
            <p><b>Price Band:</b> {ipo.price_band}</p>
            <p><b>Open:</b> {ipo.open_date}</p>
            <p><b>Close:</b> {ipo.close_date}</p>
            <p><b>Status:</b> {ipo.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
