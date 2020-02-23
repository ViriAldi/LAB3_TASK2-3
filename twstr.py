from __future__ import print_function
import twitter

CONSUMER_KEY = 'G7fuLyXrCK9hBbtKCAT8LY96T'
CONSUMER_SECRET = 'cbbcnSiKjX8A2UxRhyKf1RBPbJOZNIfyakH4ugtYbFCN8JppaC'
ACCESS_TOKEN = '1230514441420189696-EEd1see2HyRuKmcuBBGIGrTR92zI7j'
ACCESS_TOKEN_SECRET = 'Kc7iZGOFd9jzOCUAXXQSlvepXeptYDuykhf19Eunev1dT'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

name = 'iamJERAX'
users = api.GetFriends(screen_name=name)

print([u.screen_name for u in users])