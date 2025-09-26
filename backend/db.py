import sqlite3, math
from typing import List, Tuple, Dict, Any
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "climradar.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS help_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  lat REAL NOT NULL,
  lon REAL NOT NULL,
  need TEXT NOT NULL,
  priority INTEGER NOT NULL DEFAULT 2,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS volunteers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  lat REAL NOT NULL,
  lon REAL NOT NULL,
  capability TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def get_conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init():
    with get_conn() as c:
        c.executescript(SCHEMA)

def add_request(name: str, lat: float, lon: float, need: str, priority: int=2) -> int:
    with get_conn() as c:
        cur = c.execute("INSERT INTO help_requests(name,lat,lon,need,priority) VALUES(?,?,?,?,?)",
                        (name,lat,lon,need,priority))
        return cur.lastrowid

def list_requests() -> List[Dict[str,Any]]:
    with get_conn() as c:
        cur = c.execute("SELECT * FROM help_requests ORDER BY priority DESC, created_at ASC")
        return [dict(r) for r in cur.fetchall()]

def add_volunteer(name: str, lat: float, lon: float, capability: str) -> int:
    with get_conn() as c:
        cur = c.execute("INSERT INTO volunteers(name,lat,lon,capability) VALUES(?,?,?,?)",
                        (name,lat,lon,capability))
        return cur.lastrowid

def list_volunteers() -> List[Dict[str,Any]]:
    with get_conn() as c:
        cur = c.execute("SELECT * FROM volunteers ORDER BY created_at DESC")
        return [dict(r) for r in cur.fetchall()]

def _dist(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    (lat1,lon1), (lat2,lon2) = a, b
    # rough planar distance in km
    return math.hypot((lat1-lat2)*111, (lon1-lon2)*88)

def greedy_assign() -> List[Dict[str,Any]]:
    reqs = list_requests()
    vols = list_volunteers()
    assigned = []
    used = set()
    for r in reqs:
        best = None
        bestd = 1e9
        for v in vols:
            if v['id'] in used: 
                continue
            d = _dist((r['lat'], r['lon']), (v['lat'], v['lon']))
            if d < bestd:
                bestd, best = d, v
        if best:
            used.add(best['id'])
            assigned.append({"request": r, "volunteer": best, "distance_km": round(bestd,2)})
    return assigned
