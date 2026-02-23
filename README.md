# cheap_shark.py
Web-API for [cheapshark.com](https://www.cheapshark.com) website about finding the best prices on digital game downloads for PC

## Example
```python
from cheap_shark import CheapShark

cheap_shark = CheapShark()
game_info = cheap_shark.game_lookup(game_id="")
print(game_info)
```
