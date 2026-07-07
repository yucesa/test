import httpx

url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=658593d1-edc2-4f36-8d35-27e49c01c99c'

payload = {
    "msgtype": "file",
    "file": {
        "media_id": "3_3CBc1liKf0CFWIqViLMhhUbdsVTiRZYKlIcIwvz_59rlKWjsAYKaSdEx3kW5KF2"
    }
}

header = {
    "Content-Type": "application/json"
}

resp = httpx.post(url, json=payload, headers=header)

print(resp.status_code)
print(resp.text)