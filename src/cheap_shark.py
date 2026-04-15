from requests import Session

class CheapShark:
    def __init__(self) -> None:
        self.api = "https://www.cheapshark.com/api/1.0"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "Connection": "Keep-Alive"
        }

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(f"{self.api}{endpoint}", params=params).json()

    def _filter(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}

    def get_deals_list(
            self,
            store_id: str = "1",
            page_number: int = 0,
            page_size: int = 60,
            sort_by: str = "Deal Rating",
            desc: int = 0,
            lower_price: int = 0,
            upper_price: int = 15,
            metacritic: int = None,
            steam_rating: int = None,
            steam_app_id: str = None,
            title: str = None,
            exact: int = 0,
            aaa: int = 0,
            steam_works: int = 0,
            on_sale: int = 0,
            output: str = None) -> dict:
        params = self._filter({
            "storeID": store_id,
            "pageNumber": page_number,
            "pageSize": page_size,
            "sortBy": sort_by,
            "desc": desc,
            "lowerPrice": lower_price,
            "upperPrice": upper_price,
            "exact": exact,
            "AAA": aaa,
            "steamworks": steam_works,
            "onSale": on_sale,
            "metacritic": metacritic,
            "steamRating": steam_rating,
            "steamAppID": steam_app_id,
            "title": title,
            "output": output
        })
        return self._get("/deals", params)

    def deal_lookup(self, deal_id: str) -> dict:
        params = {"id": deal_id}
        return self._get("/deals", params)

    def get_games_list(
            self,
            title: str,
            steam_app_id: int,
            limit: int = 60,
            exact: int = 0) -> dict:
        params = {
            "title": title,
            "steamAppID": steam_app_id,
            "limit": limit,
            "exact": exact
        return self._get("/games", params)

    def game_lookup(self, game_id: int) -> dict:
        params = {"id": game_id}
        return self._get("/games", params)

    def games_lookup(self, game_ids: str = "128,129,130") -> dict:
        params = {"ids": game_ids}
        return self._get("/games", params)

    def get_stores_list(self) -> dict:
        return self._get("/stores")

    def edit_alert(
            self,
            action: str,
            email: str,
            game_id: int,
            price: str) -> dict:
        params = {
            "action": action,
            "email": email,
            "gameID": game_id,
            "price": price
        }
        return self._get("/alerts", params)

    def manage_alerts(self, action: str, email: str) -> dict:
        params = {
            "action": action,
            "email": email
        }
        return self._get("/alerts", params)
