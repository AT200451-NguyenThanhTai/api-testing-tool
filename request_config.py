import random

def get_header():

    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer f4b039d25e906c82c9a54af5726d8f0f00bbd1056def3ae6c985c336b93325db"
    }
# Trường hợp KHÔNG có Authorization (thiếu header)
def get_header_error1():

    return {
        "Content-Type": "application/json"
    }
# Trường hợp Authorization sai
def get_header_error2():

    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer blocked-token"
    }
def get_email():

    number = random.randint(1000,9999)

    return f"user{number}@mail.com"