import json
import random
import string
import requests


# Request URL: http://www.955599.cn/scripts/login.js?username=funincity321@gmail.com&password=hiiamagoodguy32&rand=0.017538058973099346
# Request Method: GET
i = 0
email = ""
pas = ""
letters = string.ascii_letters
digits = string.digits
url = 'http://www.955599.cn/'
with open("names.json", "r") as read_file:
    data = json.load(read_file)
while i < len(data):

    pas=""
    email = str(data[i]).lower() + random.choice(digits)+ random.choice(digits) + random.choice(digits) + random.choice(digits) + random.choice(digits) + "@gmail.com"
    pas += random.choice(letters + digits) + random.choice(letters + digits) + random.choice(letters + digits) + random.choice(letters + digits) + random.choice(letters + digits) +random.choice(letters + digits) + random.choice(letters + digits) + random.choice(letters + digits) + random.choice(letters + digits) + random.choice(letters + digits)
    requests.post(url, allow_redirects=False, data={
        'username': email,
        'password': pas
    })
    print(f'Currently sending Email: {email}             Currently Sending Password: {pas}')
    i += 1