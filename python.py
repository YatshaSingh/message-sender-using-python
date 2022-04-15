import requests
import json
url = "https://www.fast2sms.com/dev/bulk"
my_data = {
    'sender_id': 'FSTSMS', 
    'message': 'This is a test message', 
    
    'language': 'english',
    'route': 'p',
    'numbers': '9999999999, 7777777777, 6666666666'    
}
headers = {
    'authorization': 'YOUR API KEY HERE',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}
response = requests.request("POST",
                            url,
                            data = my_data,
                            headers = headers)
returned_msg = json.loads(response.text)
print(returned_msg['message'])
