import datetime

todays_date = datetime.datetime.today().date()

fields = [
    {
        "model": "restaurant.booking",
        "pk": 20,
        "fields": {
            "first_name": "Brandon Awan",
            "reservation_date": "2023-11-23",
            "reservation_slot": 14
        }
    },
    {
        "model": "restaurant.booking",
        "pk": 21,
        "fields": {
            "first_name": "Emmanuel Igbeng",
            "reservation_date": "2023-11-23",
            "reservation_slot": 15
        }
    }
]

print(f'Booking For {todays_date}')

for reservation in fields:
    print("CLIENT'S NAMES   -----------   RESERVATION DATE")
    print(f'{reservation["fields"]["first_name"]}  ----------  {todays_date}')
