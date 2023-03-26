import spotipy

CLIENT_ID = "fcc57fee73aa49f28e91fd2a9017c5bc"
CLIENT_PRIVATE_KEY = "a46b764c1b0b4948af223a5ebabe2e86"
redirect_uri ='https://www.google.com/'

scope = "user-top-read"
#scope = "user-read-currently-playing"

oauth_object = spotipy.SpotifyOAuth(client_id=CLIENT_ID,
                                    client_secret=CLIENT_PRIVATE_KEY,
                                    redirect_uri=redirect_uri,
                                    scope=scope)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

spotify_object = spotipy.Spotify(auth=token)

current = spotify_object.current_user_top_tracks(limit=50)
print(current)