import requests
import json
from venue import Venue
from performer import Performer

EVENT_BASE_URL = "https://api.seatgeek.com/2/events"
EVENTS_PER_PAGE = 500
CLIENT_ID = "NDIwNzAzNXwxNDU1Mzg0MTk1"

class Event:
    def __init__(self, event_data):
        self.listing_count = event_data['stats']['listing_count']
        self.average_price = event_data['stats']['average_price']
        self.lowest_price_good_deals = event_data['stats']['lowest_price_good_deals']
        self.lowest_price = event_data['stats']['lowest_price']
        self.highest_price = event_data['stats']['highest_price']
        self.title = event_data['title']
        self.url = event_data['url']
        self.datetime_local = event_data['datetime_local']
        self.announce_date = event_data['announce_date']
        self.visible_until_utc = event_data['visible_until_utc']
        self.time_tbd = event_data['time_tbd']
        self.date_tbd = event_data['date_tbd']
        self.performers = [Performer(performer) for performer in event_data['performers']]
        self.venue = Venue(event_data['venue'])
        self.short_title = event_data['short_title']
        self.score = event_data['score']
        self.taxonomies = event_data['taxonomies']
        self.type = event_data['type']

def get_event_data_for_id(event_id):
    response = requests.get(EVENT_BASE_URL + '/' + str(event_id)).json()
    return Event(response)

def get_event_data_for_slug(slug):
    parameters = {'performers.slug': slug}
    return get_events(parameters)

def get_event_data_for_date(date):
    parameters = {'datetime_local': date}
    return get_events(parameters)

def get_event_data_for_date_from(date):
    parameters = {'datetime_local.gte': date}
    return get_events(parameters)

def get_event_data_for_date_to(date):
    parameters = {'datetime_local.lte': date}
    return get_events(parameters)

def get_event_data_for_date_range(start_date, end_date):
    parameters = {'datetime_local.gte': start_date, 'datetime_local.lte': end_date}
    return get_events(parameters)

def get_event_data_for_venue_id(venue_id):
    parameters = {'venue.id': venue_id}
    return get_events(parameters)

def get_event_data_for_venue_state(venue_state):
    parameters = {'venue.state': venue_state}
    return get_events(parameters)

def get_event_data_for_venue_city(venue_city):
    parameters = {'venue.city': venue_city}
    return get_events(parameters)

def get_event_data_for_query(query):
    parameters = {'q': query}
    return get_events(parameters)

def get_event_data_for_taxonimy_name(name):
    parameters = {'taxonomies.name': name}
    return get_events(parameters)

def get_event_data_for_taxonimy_id(taxonomy_id):
    parameters = {'taxonomies.id': taxonomy_id}
    return get_events(parameters)

def get_events(parameters):
    parameters['client_id'] = CLIENT_ID
    parameters['per_page'] = EVENTS_PER_PAGE
    events = requests.get(EVENT_BASE_URL, params=parameters).json()
    total_results = events['meta']['total']
    page = 1
    all_events = []
    for event in events['events']:
        all_events.append(Event(event))
    while len(all_events) < total_results:
        page += 1
        parameters['page'] = page
        events = requests.get(EVENT_BASE_URL, params=parameters).json()
        for event in events['events']:
            all_events.append(Event(event))
    return all_events
