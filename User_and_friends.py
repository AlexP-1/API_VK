from urllib.parse import urlencode
import json
from pprint import pprint
import requests


def get_token():
    OAUTH_URL = 'https://oauth.vk.com/authorize'
    OAUTH_PARAMS = {
        'client_id': '7496921',
        'display': 'page',
        'scope': 'friends ',
        'response_type': 'token',
        'v': 5.107
    }

    print('?'.join(
        (OAUTH_URL, urlencode(OAUTH_PARAMS))
    ))


TOKEN = '9a34a77222018eb991f543715e2704a41e2d5bb9111f974e01af9a93a8b72ce82cb8dd4e6deb51c6590eb'


class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.params = {
            'access_token': TOKEN,
            'user_id': self.user_id,
            'v': 5.107,
            'fields': 'friends',
        }

    def __str__(self):
        return 'https://vk.com/id' + str(self.user_id)

    def user(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params=self.params
        ).json()
        friends_id = []
        for users in response['response']['items']:
            user_id = users['id']
            friends_id.append(user_id)
        friends_id_set = set(friends_id)
        return friends_id_set

    def __and__(self, other_user):
        mutal_user = self.user() & other_user.user()
        mutal_user_list = []
        for people in mutal_user:
            people = 'https://vk.com/id' + str(people)
            mutal_user_list.append(people)
        return mutal_user_list


user_1 = User(151391715)
user_2 = User(292077968)
print(f'{user_1}\n{user_2}')

mutal_user_list = user_1 & user_2
for user in mutal_user_list:
    pprint(user)
