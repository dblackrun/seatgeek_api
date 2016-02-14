# Seatgeek.com API access

See [here](http://platform.seatgeek.com/) for the SeatGeek platform documentation.
Built using python 2.7

* Clone the repository

```
cd path_to_folder
git clone https://blackport@bitbucket.org/blackport/seatgeek_api.git
```

Example: Search for Golden State Warriors games and print title and lowest price of all results

```
from seatgeek_api import event

games = event.get_event_data_for_query("golden state warriors")

for game in games:
    print game.title, game.lowest_price

```
