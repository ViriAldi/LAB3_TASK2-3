from __future__ import print_function
import twitter #pip install python-twitter
import folium #pip install folium
import geocoder #pip install geocoder
from random import randint


CONSUMER_KEY = 'G7fuLyXrCK9hBbtKCAT8LY96T'
CONSUMER_SECRET = 'cbbcnSiKjX8A2UxRhyKf1RBPbJOZNIfyakH4ugtYbFCN8JppaC'
ACCESS_TOKEN = '1230514441420189696-EEd1see2HyRuKmcuBBGIGrTR92zI7j'
ACCESS_TOKEN_SECRET = 'Kc7iZGOFd9jzOCUAXXQSlvepXeptYDuykhf19Eunev1dT'


api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def get_followers(name):
    users = api.GetFollowers(screen_name=name)
    return users


def get_friends(name):
    friends = api.GetFriends(screen_name=name)
    return friends


def locations_layer(users, name, limit):
    fg_locs = folium.FeatureGroup(name=name)

    info = [{'name': user.screen_name, 
            'loc': user.location,
            'id': user.id,
            'img': user.profile_image_url}
            for user in users]

    counter = 0
    
    for user in info:
        if counter > limit:
            break
        counter += 1

        if not user['loc']:
            continue

        point = geocoder.osm(user['loc']).osm

        if not point:
            continue

        point = (point['y'] + 0.0001 * randint(-100, 100), point['x'] + 0.0001 * randint(-100, 100))

        data = f"""
            <i>Name: {user['name']}</i>
            Location: {user['loc']}
            ID: {user['id']}
        """

        fg_locs.add_child(folium.Marker(location=point,
                                        popup=data,
                                        tooltip=user['name'],
                                        icon=folium.Icon(icon='airbnb',
                                                        prefix='fa')))

    return fg_locs


def map_creator(layers, location):
    map_loc = folium.Map(location=location,
                        zoom_start=10,
                        tiles='OpenStreetMap')

    for layer in layers:
        map_loc.add_child(layer)

    map_loc.add_child(folium.LayerControl())

    return map_loc._repr_html_()


def last_map_creator(name):
    person = api.GetUser(screen_name=name)
    locat = person.location
    point = geocoder.osm(locat).osm

    if point:
        point = (point['y'], point['x'])

    else:
        point = [0, 0]

    # followers = get_followers(pers)
    friends = get_friends(name)

    # fg_fol = locations_layer(followers, 'Followers', 100)
    fg_fri = locations_layer(friends, 'Friends', 100)

    layers = [fg_fri]

    return map_creator(layers, point)
