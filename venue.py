import requests
import json

VENUE_BASE_URL = "https://api.seatgeek.com/2/venues"

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
    parameters = {'city': city, 'per_page': 250}
    venues = requests.get(VENUE_BASE_URL, params=parameters).json()
    total_results = venues['meta']['total']
    # TODO: handle more than 250 results
    return [Venue(venue) for venue in venues['venues']]

def get_venues_for_state(state):
    parameters = {'state': state, 'per_page': 250}
    venues = requests.get(VENUE_BASE_URL, params=parameters).json()
    total_results = venues['meta']['total']
    # TODO: handle more than 250 results
    return [Venue(venue) for venue in venues['venues']]

def get_venues_for_country(country):
    parameters = {'country': country, 'per_page': 250}
    venues = requests.get(VENUE_BASE_URL, params=parameters).json()
    total_results = venues['meta']['total']
    # TODO: handle more than 250 results
    return [Venue(venue) for venue in venues['venues']]

def get_venues_for_postal_code(postal_code):
    parameters = {'postal_code': postal_code, 'per_page': 250}
    venues = requests.get(VENUE_BASE_URL, params=parameters).json()
    total_results = venues['meta']['total']
    # TODO: handle more than 250 results
    return [Venue(venue) for venue in venues['venues']]

def get_venues_for_query(query):
    parameters = {'q': query, 'per_page': 250}
    venues = requests.get(VENUE_BASE_URL, params=parameters).json()
    total_results = venues['meta']['total']
    # TODO: handle more than 250 results
    return [Venue(venue) for venue in venues['venues']]
