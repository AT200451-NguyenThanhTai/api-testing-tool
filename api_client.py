import requests
import pytest


def send_request(method, url, body=None, headers=None, expected_status=None):

    response = requests.request(
        method=method,
        url=url,
        json=body,
        headers=headers
    )
    return response