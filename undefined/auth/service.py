import requests

from rest_framework_jwt.settings import api_settings

from user.models import User
from user.serializer import UserSerializer

def get_google_user_info(access_token):
    URL = 'https://www.googleapis.com/userinfo/v2/me'
    response = requests.get(URL, headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'})
    return response.json()

def set_user_data(user, user_info):
    user.email = user_info['email']
    user.username = user_info['email'][:user_info['email'].find('@')]
    user.image = user_info['picture']
    return user

def get_user_access_token(google_access_token):
    user_info = get_google_user_info(google_access_token)
    user = set_user_data(User.objects.create(), user_info)
    user.save()

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    
    result = {}

    result['access_token'] = token
    result['email'] = user.email
    result['user_name'] = user.username
    result['image'] = user.image

    return result
