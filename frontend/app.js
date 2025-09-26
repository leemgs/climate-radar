async function post(url, data) {
  const r = await fetch(url, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data) });
  return r.json();
}
function $(id){ return document.getElementById(id); }

let lastRisk = null;

$('btnRisk').onclick = async () => {
  const payload = {
    hazard_type: $('hazard').value,
    rain_mm_per_hr: parseFloat($('rain').value||0),
    river_level_pct: parseFloat($('river').value||0),
    feels_like_c: parseFloat($('feels').value||0),
    wind_mps: parseFloat($('wind').value||0),
    lowland: $('lowland').checked,
    vulnerable_fraction: parseFloat($('vuln').value||0.0),
    calibration_k: 1.0,
    mc_trials: 500,
    uncertainty_sigma: 0.05
  };
  const out = await post('/api/risk/compute', payload);
  lastRisk = out;
  $('riskOut').textContent = JSON.stringify(out, null, 2);
}

$('btnActions').onclick = async () => {
  if (!lastRisk) { alert('Compute risk first.'); return; }
  const personas = Array.from($('personas').selectedOptions).map(o=>o.value);
  const payload = {
    hazard_type: $('hazard').value,
    risk_grade: lastRisk.risk_grade,
    personas: personas,
    language: $('lang').value
  };
  const out = await post('/api/actions/recommend', payload);
  const box = document.getElementById('actionsOut');
  box.innerHTML = '';
  out.forEach(a => {
    const div = document.createElement('div');
    div.className = 'cardlet';
    div.innerHTML = `<strong>${a.persona}</strong><br/>${a.guidance}<br/><em>${a.rationale}</em>`;
    box.appendChild(div);
  });
}

$('btnAddReq').onclick = async () => {
  const payload = {
    name: $('rq_name').value || 'citizen',
    lat: parseFloat($('rq_lat').value),
    lon: parseFloat($('rq_lon').value),
    need: $('rq_need').value,
    priority: 2
  };
  const out = await post('/api/requests', payload);
  $('reqOut').textContent = 'OK id='+out.id;
}
$('btnListReq').onclick = async () => {
  const r = await fetch('/api/requests');
  $('reqOut').textContent = JSON.stringify(await r.json(), null, 2);
}

$('btnAddVol').onclick = async () => {
  const payload = {
    name: $('vo_name').value || 'volunteer',
    lat: parseFloat($('vo_lat').value),
    lon: parseFloat($('vo_lon').value),
    capability: $('vo_cap').value
  };
  const out = await post('/api/volunteers', payload);
  $('volOut').textContent = 'OK id='+out.id;
}
$('btnListVol').onclick = async () => {
  const r = await fetch('/api/volunteers');
  $('volOut').textContent = JSON.stringify(await r.json(), null, 2);
}
$('btnAssign').onclick = async () => {
  const out = await post('/api/assign', {});
  $('volOut').textContent = JSON.stringify(out, null, 2);
}
