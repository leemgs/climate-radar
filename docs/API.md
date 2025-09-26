# API Contracts (v0.1)

## POST /api/recommendation
Request:
```json
{
  "weather_data": {"rainfall_mm_h": 70, "river_level_pct": 90},
  "location_data": {"latitude":37.5665, "longitude":126.9780},
  "vulnerability": "elderly | with_children | general"
}
```
Response:
```json
{"recommendation":"...", "reason":"...", "confidence":0.81}
```

## POST /api/checkin
```json
{"user_id":1,"status":"safe|help","location":{"latitude":..., "longitude":...}}
```

## POST /api/request_help
```json
{"user_id":1,"request_type":"medical","description":"...","location":{"latitude":..., "longitude":...}}
```

## GET /api/requests/nearby?latitude=..&longitude=..
Returns unassigned requests ordered by proximity.

## POST /api/requests/assign
```json
{"request_id": 5, "volunteer_id": 42}
```

## GET /api/dashboard/summary
Aggregates request counts; returns placeholder high‑risk areas.

## GET /api/dashboard/heatmap_data
Returns demo tiles with naive risk score based on latest weather rows.
