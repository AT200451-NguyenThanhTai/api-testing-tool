# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:19:31 2026

@author: ADMIN
"""

# kịch bản test với trường hợp thừa thiếu và sai param khi POST
# kịch bản test với trường hợp sai và thừa param khi PUT

import pytest
import api_client
import api_config
import request_config
import file

id = None
c = None
u = None


@pytest.fixture(params=[
    file.read_file("C:/Users/ACER/Documents/api_test/c_p_d.json"),  # post thừa
    file.read_file("C:/Users/ACER/Documents/api_test/c_p_t.json"),  # post thiếu
    file.read_file("C:/Users/ACER/Documents/api_test/c_p_s.json")   # post sai
])
def param_error1(request):
    global c
    c = request.param
    return c


@pytest.fixture(params=[
    file.read_file("C:/Users/ACER/Documents/api_test/u_p_d.json"),  # update thừa
    file.read_file("C:/Users/ACER/Documents/api_test/u_p_s.json")   # update sai
])
def param_error2(request):
    global u
    u = request.param
    return u


def test_post_param(param_error1):
    url = api_config.GET_URL
    headers = request_config.get_header()
    c = param_error1
    c["email"] = request_config.get_email()

    response = api_client.send_request(
        "POST",
        url,
        headers=headers,
        body=c,
        expected_status=201
    )

    re_json = response.json()
    assert response.status_code == 201
    print(re_json)
    print("API success")
def post():
    url = api_config.GET_URL
    headers = request_config.get_header()

    c_u = file.read_file("C:/Users/ACER/Documents/api_test/create.json")
    c_u["email"] = request_config.get_email()

    response = api_client.send_request(
        "POST",
        url,
        headers=headers,
        body=c_u,
        expected_status=201
    )
    re_json = response.json()
    assert response.status_code == 201
    global id
    id = re_json["id"]
    return id

def test_put_param(param_error2):
    global id

    id = post()

    url = api_config.GET_URL + f"/{id}"
    headers = request_config.get_header()

    u = param_error2

    response = api_client.send_request(
        "PUT",
        url,
        headers=headers,
        body=u,
        expected_status=200
    )

    assert response.status_code == 200
    print(response.json())
    print("API success")