from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class Spot_User(AbstractBaseUser, PermissionsMixin):
    spotify_id = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)

    USERNAME_FIELD = 'spotify_id'

# auth_backend.py
import spotipy
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class Spotify_Backend(BaseBackend):
    def authenticate(self, request, spotify_token=None):
        if spotify_token is None:
            return None

        sp = spotipy.Spotify(auth=spotify_token)
        user_info = sp.me()
        User = get_user_model()

        try:
            user = User.objects.get(spotify_id=user_info['id'])
        except User.DoesNotExist:
            user = User.objects.create_user(spotify_id=user_info['id'], access_token=spotify_token)

        return user

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None