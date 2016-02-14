import requests
import json
import event

VENUE_BASE_URL = "https://api.seatgeek.com/2/venues"
VENUES_PER_PAGE = 500

class Venue:
    def __init__(self, venue_data):
        self.city = venue_data['city']
        self.name = venue_data['name']
        self.extended_address = venue_data['extended_address']
        self.url = venue_data['url']
        self.country = venue_data['country']
        self.state = venue_data['state']
        self.score = venue_data['score']
        self.postal_code = venue_data['postal_code']
        self.location = venue_data['location']
        self.address = venue_data['address']
        self.id = venue_data['id']

def get_venue_data(venue_id):
    venue_data = requests.get(VENUE_BASE_URL + '/' + str(venue_id)).json()
    return Venue(venue_data)

def get_venues_for_city(city):
    parameters = {'city': city}
    return get_venues(parameters)

def get_venues_for_state(state):
    parameters = {'state': state}
    return get_venues(parameters)

def get_venues_for_country(country):
    parameters = {'country': country}
    return get_venues(parameters)

def get_venues_for_postal_code(postal_code):
    parameters = {'postal_code': postal_code}
    return get_venues(parameters)

def get_venues_for_query(query):
    parameters = {'q': query}
    return get_venues(parameters)

def get_venues(parameters):
    parameters['client_id'] = event.CLIENT_ID
    parameters['per_page'] = VENUES_PER_PAGE
    venues = requests.get(VENUE_BASE_URL, params=parameters).json()
    total_results = venues['meta']['total']
    page = 1
    all_venues = []
    for venue in venues['venues']:
        all_venues.append(Venue(venue))
    while len(all_venues) < total_results:
        page += 1
        parameters['page'] = page
        venues = requests.get(VENUE_BASE_URL, params=parameters).json()
        for venue in venues['venues']:
            all_venues.append(Venue(venue))
    return all_venues
