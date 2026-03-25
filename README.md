# <img src="https://www.cheapshark.com/img/logo_image.png?v=1.0" width="28" style="vertical-align:middle;" /> cheap_shark.py

> Web-API for [CheapShark](https://www.cheapshark.com) find the best prices on PC digital game downloads across multiple stores like Steam, GOG, and more.

## Quick Start
```python
from cheap_shark import CheapShark

cs = CheapShark()

# Look up a game by ID
game = cs.game_lookup(game_id=128)
print(game)
```

---

## Deals

| Method | Description |
|--------|-------------|
| `get_deals_list(store_id, page_number, page_size, sort_by, ...)` | Get a paginated list of deals with filters |
| `deal_lookup(deal_id)` | Get details for a specific deal |

**Sort by options:** `Deal Rating`, `Title`, `Savings`, `Price`, `Metacritic`, `Reviews`, `Release`, `Store`, `recent`
```python
# Get top deals under $15
cs.get_deals_list(upper_price=15, sort_by="Savings")

# Get deals for a specific store
cs.get_deals_list(store_id="1")  # 1 = Steam

# Look up a specific deal
cs.deal_lookup(deal_id="some_deal_id")
```

---

## Games

| Method | Description |
|--------|-------------|
| `get_games_list(title, steam_app_id, limit, exact)` | Search games by title or Steam ID |
| `game_lookup(game_id)` | Get all deals for a single game |
| `games_lookup(game_ids)` | Get deals for multiple games at once |
```python
# Search by title
cs.get_games_list(title="Hades", steam_app_id=1145360)

# Look up multiple games
cs.games_lookup(game_ids="128,129,130")
```

---

## Stores

| Method | Description |
|--------|-------------|
| `get_stores_list()` | Get all supported stores with IDs and info |
```python
stores = cs.get_stores_list()
for store in stores:
    print(store["storeName"], store["storeID"])
```

---

## Alerts

| Method | Description |
|--------|-------------|
| `edit_alert(action, email, game_id, price)` | Set or delete a price alert for a game |
| `manage_alerts(action, email)` | Manage all alerts for an email address |
```python
# Set an alert when a game drops below $5
cs.edit_alert(action="set", email="you@example.com", game_id=128, price="4.99")

# Delete an alert
cs.edit_alert(action="delete", email="you@example.com", game_id=128, price="4.99")

# Unsubscribe all alerts for an email
cs.manage_alerts(action="manage", email="you@example.com")
```
