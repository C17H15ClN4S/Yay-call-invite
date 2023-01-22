import requests

token = ""
call_id = ""
user_id = ""

r = requests.post(
    f"https://api.yay.space/v1/calls/conference_calls/{call_id}/invite"
    , headers={
        "authorization": f"{token}",
        "content-type": "application/json;charset=UTF-8"
    }
    , json={
        "user_ids": [f"{user_id}"]
    })

print(r.status_code,r.json())