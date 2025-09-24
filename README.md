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
