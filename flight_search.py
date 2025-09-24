import requests
from data_manager import DataManager
from data import URL_SHEETY, NAME, PASSWORD, AUTHORIZATION, API_KEY, API_SECRET, URL_IATA, URL_ENDPOINT

parameters = {
    'Username': NAME,
    'Password': PASSWORD,
}
header = {
    'Authorization': AUTHORIZATION,
}

class FlightSearch(DataManager):
    def __init__(self):
        super().__init__(URL_SHEETY, parameters, header)
        self.cities = []
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.api_token = self.get_new_token()

    def fill_code(self):
        if DataManager.is_data_empty(self):
            for index in range(len(self.cities)):
                self.sheet_data[index]['iataCode'] = self.cities[index]
            return self.sheet_data
        else:
            return None

    def get_new_token(self):
        header_1 = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(URL_ENDPOINT, headers=header_1, data=body)
        response.raise_for_status()
        return response.json()['access_token']

    def generate_codes(self):
        headers = {
            'Authorization': f'Bearer {self.api_token}',
        }
        for row in self.sheet_data:
            parameters_1 = {
                'keyword': row['city'].upper(),
                'max': 1,
                'include': 'AIRPORTS'
            }
            response = requests.get(URL_IATA, params=parameters_1, headers=headers)
            response.raise_for_status()

            if not bool(response):
                self.cities.append('N/A')
            else:
                self.cities.append(response.json()['data'][0]['iataCode'])
        print(self.cities)