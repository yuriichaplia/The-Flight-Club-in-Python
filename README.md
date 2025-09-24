# The Flight Club in Python
This project is an upgraded version of a Cheap Flight Notifier that automatically checks for cheaper flight prices and sends alerts via SMS and email.

Users provide their emails through a Google Form, which is connected to a Google Spreadsheet. The spreadsheet also contains destination cities and a "lowest price" threshold. If a cheaper flight is found, the system notifies all users and the owner’s phone number.

## Features
+ Fetches user emails from Google Spreadsheet (via Sheety API)
+ Retrieves flight information using the Amadeus API
+ Automatically fills in missing IATA airport codes
+ Compares live flight prices with thresholds in the spreadsheet
+ Sends alerts when cheaper flights are available: SMS via Twilio and Email via Gmail SMTP
+ Manages secrets with .env environment variables

## Create a .env file in the root folder with the following variables:
NAME=your_sheety_basicauthentication_username <br>
PASSWORD=your_sheety_basicauthentication_password<br>
AUTHORIZATION=your_sheety_auth_token<br>
URL_SHEETY=https://api.sheety.co/your_project/prices<br>
USER_SHEETY=https://api.sheety.co/your_project/users<br>
API_KEY=your_amadeus_api_key<br>
API_SECRET=your_amadeus_api_secret<br>
ACC_SID=your_twilio_account_sid<br>
AUTH_TOKEN=your_twilio_auth_token<br>
TWILIO_PHONE_NUMBER=+1234567890<br>
PHONE_NUMBER=+0987654321   # Your phone to receive alerts<br>
MY_EMAIL=youremail@gmail.com<br>
EMAIL_PASSWORD=your_gmail_app_password

##### Note that you also should create a google form with 3 questions (e.g. What's your first/last name and email), then connect it to your spreadsheet, rename it to users and fill it with emails (you can copy link to the form open it in incognito mode and add your emails). 

