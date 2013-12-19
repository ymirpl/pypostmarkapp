# encoding: utf8

text = """text to scan for emails"""

import re, sys, requests
import pystmark, simplejson as json


API_KEY = 'POSTMARK_API_KEY'
SENDER = "POSTMARK_SENDER"
MSG = """email contents"""


def send_email_req(messages):
    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json",
        "X-Postmark-Server-Token": API_KEY
    }
    r = requests.post("http://api.postmarkapp.com/email/batch",
        headers=headers,
        data=messages)

    print r
 
email_pattern = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)') # Look for emails in `text` using regular expression
recipients = list()
jsons = list()

for line in text.splitlines():
    # print line

    for match in email_pattern.findall(line): # append found email to recipients list
            recipients.append(match[0])

for r in recipients:
    jsons.append({
        'From': SENDER, 
        'To': r, 
        'Subject': "subject", 
        'TextBody': MSG, 
    })

send_email_req(json.dumps(jsons, encoding="utf-8")) # send email to all recipients using Postmarkapp batch API
