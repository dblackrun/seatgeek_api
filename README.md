# Seatgeek.com API access

See [here](http://platform.seatgeek.com/) for the SeatGeek platform documentation.

See [SeatGeek API terms](https://seatgeek.com/api-terms) before using.

Get a client id from [here](https://seatgeek.com/account/develop)

Built using python 2.7

* Clone the repository

```
cd path_to_folder
git clone https://github.com/dblackrun/seatgeek_api.git
```


* Enter your client id in event.py
```
CLIENT_ID = your client id here
```

Example: Search for Golden State Warriors games and print title and lowest price of all results

```
from seatgeek_api import event

games = event.get_event_data_for_query("golden state warriors")

for game in games:
    print game.title, game.lowest_price

```
