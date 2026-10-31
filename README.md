# Metro route planner: A* API

University project (UPM, 2024). Python API that finds the fastest route between two stations of the Buenos Aires Subte (central network: lines A to E, 37 stations) and turns it into a timed itinerary.

**Live app:** [appmetro.vercel.app](https://appmetro.vercel.app) · **Frontend:** [python-metro-frontend](https://github.com/SergioMedinaH/python-metro-frontend)

## How it works

1. **Graph.** Stations are nodes in a NetworkX graph; each edge is a track segment or a transfer between lines, weighted by the real distance between stations (Haversine on their coordinates).
2. **Search.** The route is found with **A\***, using the straight-line distance to the destination as the heuristic. It never overestimates the remaining distance, so A* returns the shortest path while exploring fewer nodes than Dijkstra.
3. **Itinerary.** The path is split into legs per line. For each leg the API computes the direction, the next departure from the timetable (first train plus weekday or weekend frequency), the waiting time and the arrival time. Transfers add their measured walking time.
4. **Station data** comes from a CSV: coordinates, line, first trains in each direction for weekdays, Saturdays and Sundays, frequencies, travel time to the next station, and accessibility (stairs, escalators, lifts).

## API

```
GET /api?paradaOrigen=alberti&paradaDestino=retiroe&hora=10:00&fecha=1
```

| Parameter | Meaning |
|---|---|
| `paradaOrigen`, `paradaDestino` | Station ids (see `data/paradas.csv`) |
| `hora` | Departure time, `HH:MM` |
| `fecha` | Day of the week, 0 = Sunday … 6 = Saturday |

The response includes the station sequence, the legs with departure and arrival times, the total duration and the arrival time.

## Stack

Python · NetworkX · pandas · Vercel serverless functions

## Run locally

```bash
pip install -r requirements.txt
vercel dev
```
