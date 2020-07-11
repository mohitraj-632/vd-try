import requests
import json
import time
from datetime import datetime
from lomond import WebSocket
from unidecode import unidecode
import colorama
import re
from dhooks import Webhook, Embed
import websocket
import random
import base64
from websocket import create_connection	
from bs4 import BeautifulSoup

bearer = "eyJhbGciOiJIUzl1NilslnR5cCl6lkpXVCJ9.eyJ1c2VybmFtZSI6lk1vaGloiFJhailsinVzZxJfdWIkljoiNDEWMjQOMTk30DY4MzgxNSIslmF2YXRhcil6lilslmV4cCI6MTU5NDQ3NTgxMSwiaWFOljoxNTkONDcOMDExLCJfX2FwcCI6InZIZGFudHUifQ.Vn02pu5DyWbRIS32mElW_brOEwsNMTqKejqWP_OAUXY"
webhook_url = "https://discordapp.com/api/webhooks/731515307939856385/EWR3jDN-rcTWZipIN-VwxmcM3WM8Fc6PWsHSOHk9y-JQy1AkCBLOBcpMd5hiB9u7Nkge"

hook = Webhook(webhook_url)
try:
	hook = Webhook(webhook_url)
except:
	print("Invalid WebHook Url!")

url = "https://vedantuapi.getloconow.com/v2/vendors/vedantu/v1/contest/"

headers = {
	'Host':'vedantuapi.getloconow.com',
	'x-app-version':'100015',
	'x-platform':'5',
	'device-id':'30193B7938EA504EB77D3B67c8352FE431286AE9',
	'x-app-language':'1',
	'ipn:':'com.vedantu.app',
	'client-id':'CagkWJoLLYEY2FK9Ve2XqvekDkDDIITJnYkhpmfT',
	'client-secret':'jbwPDmTe6eHSFnf7qSMOrQdOqZ1X05yoLPCw5jyGeXmRmmSi1hwRIYX7uFTuXdSmWcjfjrujFTnZM6UhXBUE7SGEg3zHgtH2nLk3Pxg6tAhD1Cyzlt590Rtl8T5GFJ0s',
	'authorization':'Bearer eyJhbGciOiJIUzl1NilslnR5cCl6lkpXVCJ9.eyJ1c2VybmFtZSI6lk1vaGloiFJhailsinVzZxJfdWIkljoiNDEWMjQOMTk30DY4MzgxNSIslmF2YXRhcil6lilslmV4cCI6MTU5NDQ3NTgxMSwiaWFOljoxNTkONDcOMDExLCJfX2FwcCI6InZIZGFudHUifQ.Vn02pu5DyWbRIS32mElW_brOEwsNMTqKejqWP_OAUXY',
	'accept-encoding':'gzip',
	'user-agent':'okhttp/3.14.4'
}

r = requests.get(url,headers=headers).json()
print(r)
