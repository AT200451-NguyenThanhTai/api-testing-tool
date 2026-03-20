# Kịch bản test với trường hợp sai Authorization và không có Authorization
import pytest
import api_config
import api_client
import request_config
import file

id = None
id_1 = None
id_2 = None

# Fixture để cung cấp header với authorization sai hoặc không có authorization
@pytest.fixture(params=[
    request_config.get_header_error1(),  # Trường hợp không có Authorization
    request_config.get_header_error2()   # Trường hợp Authorization sai
])
def auth_error_header(request):
    return request.param

def post():

    url = api_config.GET_URL
    headers = request_config.get_header()

    c_u = file.read_file("C:/Users/ACER/Documents/api_test/create.json")
    c_u["email"] = request_config.get_email()

    response = api_client.send_request(
        "POST",
        url,
        body=c_u,
        headers=headers
    )

    re_json = response.json()

    assert response.status_code == 201

    global id
    id = re_json["id"]
    return id


# -------- GET --------
def test_get_auth(auth_error_header):

    url = api_config.GET_URL
    headers = auth_error_header

    response = api_client.send_request(
        "GET",
        url,
        headers=headers
    )

    assert response.status_code == 200
    print(response.json())
    print("API success")


# -------- POST --------
def test_post_auth(auth_error_header):

    url = api_config.GET_URL
    headers = auth_error_header

    c_u = file.read_file("C:/Users/ACER/Documents/api_test/create.json")
    c_u["email"] = request_config.get_email()

    response = api_client.send_request(
        
        "POST",
        url,
        body=c_u,
        headers=headers
    )

    re_json = response.json()

    assert response.status_code == 201

    global id
    id = re_json["id"]

    print(re_json)
    print("API success")


# -------- PUT --------
def test_put_auth(auth_error_header):

    global id
    global id_1
    global id_2

    if auth_error_header == request_config.get_header_error2():
        id_2 = post()
        id = id_2

    if auth_error_header == request_config.get_header_error1():
        id_1 = 8399261
        id = id_1

    url = api_config.GET_URL + f"/{id}"
    headers = auth_error_header

    c_u = file.read_file("C:/Users/ACER/Documents/api_test/update.json")

    response = api_client.send_request(
        "PUT",
        url,
        body=c_u,
        headers=headers
    )

    assert response.status_code == 200
    print(response.json())
    print("API success")


# -------- DELETE --------
def test_delete_auth(auth_error_header):

    global id
    global id_1
    global id_2

    if auth_error_header == request_config.get_header_error2():
        id = id_2

    if auth_error_header == request_config.get_header_error1():
        id = id_1

    url = api_config.GET_URL + f"/{id}"
    headers = auth_error_header

    response = api_client.send_request(
        "DELETE",
        url,
        headers=headers
    )

    assert response.status_code == 204
    print("API success")