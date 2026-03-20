# kịch bản test POST trùng id, trùng email, sai định dạng email

import pytest
import api_config
import api_client
import request_config
import file

c_u = None

@pytest.fixture(params=[
    file.read_file("C:/Users/ACER/Documents/api_test/c_d_id.json"),       # post trùng id
    file.read_file("C:/Users/ACER/Documents/api_test/c_d_email_1.json"),  # post trùng email
    file.read_file("C:/Users/ACER/Documents/api_test/c_d_email_2.json")   # post sai định dạng email
])
def data_error(request):
    global c_u
    c_u = request.param
    return c_u

def test_post_data(data_error):

    url = api_config.GET_URL
    headers = request_config.get_header()

    c_u = data_error

    # nếu test trùng id thì tạo email random để tránh lỗi email trùng
    if "id" in c_u:
        c_u["email"] = request_config.get_email()

    response = api_client.send_request(
        "POST",
        url,
        body=c_u,
        headers=headers
    )
    re_json = response.json()
    assert response.status_code == 201
    print(re_json)
    print("API success")