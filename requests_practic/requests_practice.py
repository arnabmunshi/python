# pip install requests
import requests
import json

# res = requests.get('https://viswakarmawelfare.org/api/queries')
# print(res.text)cls

payload = {'member_id': 1, 'query': 'Sync From Local to Cloud'}
res = requests.post('https://viswakarmawelfare.org/api/queries', data=payload)
print(res.text)
