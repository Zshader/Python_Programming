import requests as r
import json
import base64
from dotenv import load_dotenv

import os

load_dotenv()

oauth_token=os.getenv("OAUTH_TOKEN")

print(oauth_token)

# GET_Request
#Get all repositories from Github
# base_url = "https://api.github.com/user/repos"

# response = r.get(base_url,
#            headers={'Authorization': 'token {}'.format(oauth_token)}
#            )

# # print(response.json(),"\n")

# for x in response.json():
#     print(x["full_name"])


#Post Requests

base_url = "https://api.github.com/user/repos"

config = {"name":"PythonRequestTutorial",
    "auto_init": True,
    "private":False,
    "gitignoretemplate": "nonoc"}

config_to_send=json.dumps(config)

response = r.post(base_url,data = config_to_send,
            headers={'Authorization': 'token {}'.format(oauth_token)})

print(response.status_code)
print(response.json())


