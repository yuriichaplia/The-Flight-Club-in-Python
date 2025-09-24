import requests
from data import USER_SHEETY

class DataManager:
    def __init__(self, url, parameters, header):
        self.url = url
        self.parameters = parameters
        self.header = header
        self.sheet_data = self.get_data()
        self.user_emails = []


    def send_request(self):
        request = requests.get(self.url, params=self.parameters, headers=self.header)
        request.raise_for_status()
        return request

    def get_data(self):
        print(self.send_request().json()['prices'])
        return self.send_request().json()['prices']

    def is_data_empty(self):
        is_empty = True
        empty_number = 0
        for element in self.sheet_data:
            print(element['iataCode'])
            if element['iataCode'] == '':
                empty_number += 1
        if empty_number == 0:
            is_empty = False
        print(is_empty)
        return is_empty

    def put_code(self, index, json_data):
        request = requests.put(f'{self.url}/{index}', json = json_data, headers=self.header)
        request.raise_for_status()

    def get_customer_email(self):
        request = requests.get(f'{USER_SHEETY}', params=self.parameters, headers=self.header)
        request.raise_for_status()
        data = request.json()
        for element in data['users']:
            self.user_emails.append(element['whatIsYourEmail?'])

        return data