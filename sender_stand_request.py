import configuration
import data
import requests


def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)


response = post_new_user(data.user_body)


def post_new_kit_for_user(body):

    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH, json=body, headers=data.headers_for_kits)


response = post_new_kit_for_user(data.kit_body)

