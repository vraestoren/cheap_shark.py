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
            AAA: int = 0,
            steam_works: int = 0,
            on_sale: int = 0,
            output: str = None) -> dict:
        params = {
            "pageNumber": page_number,
            "pageSize": page_size,
            "sortBy": sort_by,
            "desc": desc,
            "lowerPrice": lower_price,
            "upperPrice": upper_price,
            "exact": exact,
            "AAA": AAA,
            "steamworks": steam_works,
            "onSale": on_sale,
            "metacritic": metacritic,
            "steamRating": steam_rating,
            "steamAppID": steam_app_id,
            "title": title,
            "output": output
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.get(
            f"{self.api}/deals?storeID={store_id}", params=filtered_params).json()

    def deal_lookup(self, deal_id: str) -> dict:
        return self.session.get(
            f"{self.api}/deals?id={deal_id}").json()
    
    def get_games_list(
            self,
            title: str,
            steam_app_id: int,
            limit: int = 60,
            exact: int = 0) -> dict:
        return self.session.get(
            f"{self.api}/games?title={title}&steamAppID={steam_app_id}&limit={limit}&exact={exact}").json()
    
    def game_lookup(self, game_id: int) -> dict:
        return self.session.get(
            f"{self.api}/games?id={game_id}").json()
    
    def games_lookup(self, game_ids: str = "128,129,130") -> dict:
        return self.session.get(
            f"{self.api}/games?ids={game_ids}").json()
    
    def get_stores_list(self) -> dict:
        return self.session.get(
            f"{self.api}/stores").json()
    
    def edit_alert(
            self,
            action: str,
            email: str,
            game_id: int,
            price: str) -> dict:
        return self.session.get(
            f"{self.api}/alerts?action={action}&email={email}&gameID={game_id}&price={price}").json()
    
    def manage_alerts(
            self,
            action: str,
            email: str) -> dict:
        return self.session.get(
            f"{self.api}/alerts?action={action}&email={email}").json()
