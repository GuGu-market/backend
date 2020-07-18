import requests
from datetime import datetime

from rest_framework_jwt.settings import api_settings

from user.models import User
from point.models import Point

from user.serializer import UserSerializer
from point.serializer import PointSerializer

def get_google_user_info(access_token):
    URL = 'https://www.googleapis.com/userinfo/v2/me'
    response = requests.get(URL, headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'})
    return response.json()

def init_user_data(user_info, created_at):
    data = {}
    data['id'] = ''
    data['email'] =  user_info['email']
    data['username'] =  user_info['email'][:user_info['email'].find('@')]
    data['image'] =  user_info['picture']
    data['activate'] =  True
    data['grade'] = 0
    data['phone'] =  ''
    data['created_at'] = created_at

    return data

def init_user_point(user_info, user_id, created_at):
    data = {}

    data['id'] = ''
    data['user_id'] = user_id
    data['username'] = user_info['email'][:user_info['email'].find('@')]
    data['point_amount'] = 0
    data['created_at'] = created_at
    data['updated_at'] = created_at

    return data

def get_user_access_token(google_access_token):
    created_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    user_info = get_google_user_info(google_access_token)

    user_data = init_user_data(user_info, created_at)
    user_model = User.objects.create(username=user_data['username'], email=user_data['email'], image=user_data['image'])
    user_serializer = UserSerializer(user_model, data=user_data)
    
    if user_serializer.is_valid():
        user_serializer.create()

    point_data = init_user_point(user_info, user_model.id, created_at)
    point_model = Point.objects.create(user_id=user_model.id)
    point_serializer = PointSerializer(point_model, data=point_data)

    if point_serializer.is_valid():
        point_serializer.create()

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user_model)
    token = jwt_encode_handler(payload)
    
    result = {}

    result['access_token'] = token
    result['email'] = user_model.email
    result['user_name'] = user_model.username
    result['image'] = user_model.image

    return result
