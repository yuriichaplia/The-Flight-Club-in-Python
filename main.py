from data import NAME, PASSWORD, AUTHORIZATION
from notification_manager import NotificationManager

parameters = {
    'Username': NAME,
    'Password': PASSWORD,
}
header = {
    'Authorization': AUTHORIZATION,
}

notifications = NotificationManager()

notifications.get_data()
notifications.generate_codes()

if notifications.fill_code() is not None:
    for row in notifications.sheet_data:
        print(row)
        json_data = {
            'price': {
                'iataCode': row['iataCode'],
            }
        }
        notifications.put_code(row['id'], json_data)

notifications.find_flight()
notifications.compare_prices()
notifications.send_message()

notifications.get_customer_email()
for element in notifications.user_emails:
    notifications.send_emails(element)