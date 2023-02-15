from . import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from spotipy import util

def login(request):
    redirect_uri = request.build_absolute_uri(reverse('spotify_callback'))
    scope = 'user-read-email user-library-read'
    auth_url = util.oauth2.SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=redirect_uri,
        scope=scope
    ).get_authorize_url()

    return redirect(auth_url)
def spotify_callback(request):
    sp_oauth = util.oauth2.SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=request.build_absolute_uri(reverse('spotify_callback')),
        scope='user-read-email user-library-read'
    )

    code = request.GET.get('code', None)
    if code is not None:
        token_info = sp_oauth.get_access_token(code)
        spotify_token = token_info['access_token']

        backend = models.Spotify_Backend()
        user = backend.authenticate(request, spotify_token=spotify_token)

        if user is not None:
            login(request, user)
            return redirect(reverse('home'))

    # handle authentication failure
    return HttpResponse('Authentication failed.')
