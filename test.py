
import requests
from http import HTTPStatus


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

req = requests.get("https://amazon.com", headers=headers)
print(req.status_code)


def get_status_des(status_code):
    for value in HTTPStatus:
        if value == status_code:
            des = f"({value} {value.name}), {value.description}"

            print(des)

    return "(???) Unknown Status Code!!!"

get_status_des(200)