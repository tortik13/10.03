from requests import get

print(get('http://127.0.0.1:5003/api/jobs').json())