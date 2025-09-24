import requests
from data import FLIGHT_OFFERS
from flight_search import FlightSearch
from datetime import datetime, timedelta


class FlightData(FlightSearch):
    def __init__(self):
        super().__init__()
        self.url_flights = FLIGHT_OFFERS
        self.data = {}

    def find_flight(self):
        dep_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        ret_date = (datetime.today() + timedelta(days=1) + timedelta(days=180)).strftime("%Y-%m-%d")

        headers = {
            'Authorization': f'Bearer {self.api_token}',
        }

        for element in self.sheet_data:
            parameters = {
                'originLocationCode': 'LON',
                'destinationLocationCode': element['iataCode'],
                'departureDate': dep_date,
                'returnDate': ret_date,
                'adults': 1,
                'nonStop': 'true',
                'currencyCode': 'GBP'
                }

            try:
                response = requests.get(self.url_flights, params=parameters, headers=headers)
                response.raise_for_status()
                period = response.json()

                if not period['data']:
                    parameters = {
                        'originLocationCode': 'LON',
                        'destinationLocationCode': element['iataCode'],
                        'departureDate': dep_date,
                        'returnDate': ret_date,
                        'adults': 1,
                        'nonStop': 'false',
                        'currencyCode': 'GBP'
                    }
                    response = requests.get(self.url_flights, params=parameters, headers=headers)
                    response.raise_for_status()
                    period = response.json()

            except requests.exceptions.HTTPError:
                self.update_data(element['iataCode'], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')
            else:
                if not period['data']:
                    self.update_data(element['iataCode'], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')
                else:
                    try:
                        self.find_cheapest_flight(0, period, element['iataCode'])
                    except IndexError:
                        self.find_cheapest_flight(1, period, element['iataCode'])

    def find_cheapest_flight(self, index, period, code):
        if period["data"]:
            cheapest_flight = period["data"][0]["price"]["total"]
            origin_airport = period['data'][index]['itineraries'][0]['segments'][0]['departure']['iataCode']
            destination_airport = period['data'][index]['itineraries'][0]['segments'][len(period["data"][index]["itineraries"][0]['segments'])-1]['arrival']['iataCode']
            out_date = period['data'][index]['itineraries'][0]['segments'][0]['departure']['at']
            return_date = period['data'][index]['itineraries'][0]['segments'][0]['arrival']['at']
            stops = len(period["data"][index]["itineraries"][0]['segments'])-1
            for element_1 in period['data']:
                if element_1['price']['total'] < cheapest_flight:
                    cheapest_flight = element_1['price']['total']
                    origin_airport = element_1['itineraries'][0]['segments'][0]['departure']['iataCode']
                    destination_airport = element_1['itineraries'][0]['segments'][len(element_1["itineraries"][0]['segments'])-1]['arrival']['iataCode']
                    out_date = element_1['itineraries'][0]['segments'][0]['departure']['at']
                    return_date = element_1['itineraries'][1]['segments'][0]['departure']['at']
                    stops = len(element_1["itineraries"][0]['segments'])-1
            self.update_data(code, cheapest_flight, origin_airport, destination_airport, out_date, return_date, stops)
        else:
            self.update_data(code, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')

    def update_data(self, name, cheapest_flight, origin_airport, destination_airport, out_date, return_date, stops):
        self.data.update({name: {
            'price': cheapest_flight,
            'origin_airport': origin_airport,
            'destination_airport': destination_airport,
            'outdate': out_date,
            'arrival': return_date,
            'stops': stops
        }})