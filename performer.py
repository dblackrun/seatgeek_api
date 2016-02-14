import requests
import json

PERFORMER_BASE_URL = "https://api.seatgeek.com/2/performers"

class Performer:
    def __init__(self, performer_data):
        self.name = performer_data['name']
        self.short_name = performer_data['short_name']
        self.url = performer_data['url']
        self.image = performer_data['image']
        self.images = performer_data['images']
        self.score = performer_data['score']
        self.slug = performer_data['slug']
        self.taxonomies = performer_data['taxonomies']
        self.has_upcoming_events = performer_data['has_upcoming_events']
        self.id = performer_data['id']

def get_performer_data_for_id(performer_id):
    parameters = {'id': performer_id}
    performer_data = requests.get(PERFORMER_BASE_URL, params=parameters).json()
    return Performer(performer_data['performers'][0])

def get_performer_data_for_slug(slug):
    parameters = {'slug': slug}
    performer_data = requests.get(PERFORMER_BASE_URL, params=parameters).json()
    return Performer(performer_data['performers'][0])

def get_performer_data_for_taxonomy_name(taxonomy_name):
    parameters = {'taxonomies.name': taxonomy_name, 'per_page': 250}
    performers = requests.get(PERFORMER_BASE_URL, params=parameters).json()
    # TODO: handle more than 250 results
    return [Performer(performer) for performer in performers['performers']]

def get_performer_data_for_taxonomy_id(taxonomy_id):
    parameters = {'taxonomies.id': taxonomy_id, 'per_page': 250}
    performers = requests.get(PERFORMER_BASE_URL, params=parameters).json()
    # TODO: handle more than 250 results
    return [Performer(performer) for performer in performers['performers']]
