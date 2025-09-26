import React, { useEffect, useState } from 'react'

export default function App() {
  const [summary, setSummary] = useState(null)
  const [heatmap, setHeatmap] = useState(null)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/dashboard/summary').then(r=>r.json()).then(setSummary)
    fetch('http://127.0.0.1:8000/api/dashboard/heatmap_data').then(r=>r.json()).then(setHeatmap)
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', padding: 24 }}>
      <h2>Climate RADAR — Institutional Dashboard</h2>
      <section style={{ marginBottom: 24 }}>
        <h3>Summary</h3>
        <pre style={{ background:'#f6f6f6', padding: 12 }}>{JSON.stringify(summary, null, 2)}</pre>
      </section>
      <section>
        <h3>Heatmap Tiles (demo)</h3>
        <pre style={{ background:'#f6f6f6', padding: 12 }}>{JSON.stringify(heatmap, null, 2)}</pre>
      </section>
    </div>
  )
}
