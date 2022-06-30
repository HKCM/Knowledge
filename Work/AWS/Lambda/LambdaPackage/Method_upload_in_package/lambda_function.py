import json
import urllib3


def lambda_handler(event, context):
    http = urllib3.PoolManager()
    response = http.request('GET','www.baidu.com',headers = {'Content-Type': 'application/json'})
    print(response.status)
    return response.status
    #response.data.decode()