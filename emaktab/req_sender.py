import uuid

import requests


def auto_post(user_login,user_pass):
    url = "https://login.emaktab.uz/login"
    captcha=str(uuid.uuid4())
    data = {
        "exceededAttempts": "False",
        "ReturnUrl": "",
        "FingerprintId": "",
        "login": {user_login},
        "password": {user_pass},
        "Captcha.Input": {captcha},
        "Captcha.Id":id
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("So'rov muvaffaqiyatli jo'natildi.")
        return True
    else:
        print("Xatolik yuz berdi:", response.status_code)
        return False
