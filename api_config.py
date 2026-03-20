import json

def get_base_url():
    with open(r"C:\Users\ACER\Documents\api_test\environment.json") as f:
        config = json.load(f)

    env = config["environment"]["env"]
    return config[env]["base_url"]


GET_URL = get_base_url() + "/public/v2/users"