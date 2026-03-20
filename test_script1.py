import pytest
import api_config
import api_client
import request_config
import file

user_id = None


def test_get():

    url = api_config.GET_URL
    headers = request_config.get_header()

    response = api_client.send_request(
        "GET",
        url,
        headers=headers,
        
    )

    assert response.status_code == 200

    print(response.json())
    print("API success")

    file.write_file("C:/Users/ACER/Documents/api_test/start.json", response.json())


def test_post():

    url = api_config.GET_URL
    headers = request_config.get_header()

    c_u = file.read_file("C:/Users/ACER/Documents/api_test/create.json")
    c_u["email"] = request_config.get_email()
    response = api_client.send_request(
        "POST",
        url,
        body=c_u,
        headers=headers,
        
    )
    assert response.status_code == 201
    re_json = response.json()
    
    global user_id 
    user_id = re_json["id"]
    

    print(re_json)
    print("API success")


def test_put():

    global user_id

    url = api_config.GET_URL + f"/{user_id}"
    headers = request_config.get_header()

    c_u = file.read_file("C:/Users/ACER/Documents/api_test/update.json")

    response = api_client.send_request(
        "PUT",
        url,
        body=c_u,
        headers=headers,
        
    )
    assert response.status_code == 200

    print(response.json())
    print("API success")


def test_delete():

    global user_id

    url = api_config.GET_URL + f"/{user_id}"
    headers = request_config.get_header()

    response = api_client.send_request(
        "DELETE",
        url,
        headers=headers,
        
    )
    assert response.status_code == 204

    print("API success")