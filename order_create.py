<<<<<<< HEAD
import requests
import data
import configuration

def create_order():
    response = requests.post(configuration.url + configuration.url_order, json=data.order_body)
    return response.json()['track']


def get_track():
    track_number = create_order()
    response = requests.get(configuration.url + configuration.url_track + str(track_number))
=======
import requests
import data
import configuration

def create_order():
    response = requests.post(configuration.url + configuration.url_order, json=data.order_body)
    return response.json()['track']


def get_track():
    track_number = create_order()
    response = requests.get(configuration.url + configuration.url_track + str(track_number))
>>>>>>> 8a4d2a0453e5bd83c39baaebf0ab4996897e95a6
    return response