import smtplib
from twilio.rest import Client
from flight_data import FlightData
from data import ACC_SID, AUTH_TOKEN, MY_EMAIL, EMAIL_PASSWORD, PHONE_NUMBER, TWILIO_PHONE_NUMBER

class NotificationManager(FlightData):
    def __init__(self):
        super().__init__()
        self.message = []
        self.account_sid = ACC_SID
        self.auth_token = AUTH_TOKEN
        self.my_email = MY_EMAIL
        self.my_password = EMAIL_PASSWORD
        self.notification = ""

    def compare_prices(self):
        for element in self.sheet_data:
            name = element['iataCode']
            if self.data[name]['price'] != 'N/A':
                if element['lowestPrice'] > round(float(self.data[name]['price']), 2):
                    self.message.append(self.data[name])

    def send_message(self):
        client = Client(self.account_sid, self.auth_token)

        for index in range(len(self.message)):
            if self.message[index]['stops'] != 0:
                self.notification += f"Only {self.message[index]['price']} from LON to {self.message[index]['destination_airport']} on {self.message[index]['outdate']} at {self.message[index]['stops']} stop(s). "
            else:
                self.notification += f"Only {self.message[index]['price']} from LON to {self.message[index]['destination_airport']} on {self.message[index]['outdate']}. "

        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=f'Low Price Alert! {self.notification}',
            to=PHONE_NUMBER
        )

        print(message.sid)

    def send_emails(self, email):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=email,
                msg=f'Subject:Cheap Flights!\n\n{self.notification}')