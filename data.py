from os import environ
from dotenv import load_dotenv

load_dotenv()

NAME = environ["NAME"]
ACC_SID = environ["ACC_SID"]
API_KEY = environ["API_KEY"]
PASSWORD = environ["PASSWORD"]
MY_EMAIL = environ["MY_EMAIL"]
URL_SHEETY = environ["URL_SHEETY"]
AUTH_TOKEN = environ["AUTH_TOKEN"]
API_SECRET = environ["API_SECRET"]
USER_SHEETY = environ["USER_SHEETY"]
PHONE_NUMBER = environ["PHONE_NUMBER"]
AUTHORIZATION = environ["AUTHORIZATION"]
EMAIL_PASSWORD = environ["EMAIL_PASSWORD"]
TWILIO_PHONE_NUMBER = environ["TWILIO_PHONE_NUMBER"]
URL_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_OFFERS = "https://test.api.amadeus.com/v2/shopping/flight-offers"
URL_IATA = "https://test.api.amadeus.com/v1/reference-data/locations/cities"