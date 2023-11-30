import configuration
import data
import requests


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)


def get_new_user_token():
    response = post_new_user(data.user_body)
    dato = response.json()
    return dato['authToken']


def post_new_kit_for_user(body):
    authToken = get_new_user_token()
    headers = {"Content-Type": "application/json",
        "Authorization": f"Bearer {authToken}"}
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH, json=body, headers=headers)
