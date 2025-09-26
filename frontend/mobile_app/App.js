import React, { useState } from 'react';

export default function App() {
  const [message, setMessage] = useState('');
  const [rec, setRec] = useState(null);

  const requestRecommendation = async () => {
    const payload = {
      weather_data: { rainfall_mm_h: 70, river_level_pct: 90 },
      location_data: { latitude: 37.5665, longitude: 126.9780 },
      vulnerability: 'general'
    };
    const res = await fetch('http://127.0.0.1:8000/api/recommendation', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    setRec(data);
  };

  return (
    <div style={{ fontFamily: 'sans-serif', padding: 24 }}>
      <h2>Climate RADAR — Citizen Demo</h2>
      <button onClick={requestRecommendation}>Get Action Recommendation</button>
      {rec && (
        <pre style={{ background: '#f6f6f6', padding: 16, marginTop: 12 }}>
{JSON.stringify(rec, null, 2)}
        </pre>
      )}
    </div>
  );
}
