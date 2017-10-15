#!notify/bin/python3

import os
import sys
from pushbullet import Pushbullet


def create_note(title, content):
    api_key = os.environ["PB_API_KEY"]
    pb = Pushbullet(api_key)
    pb.push_note(title, content)


if len(sys.argv) >= 3:
    title = sys.argv[1]
    body = sys.argv[2]
    create_note(title, body)
else:
    print("Error: Missing arguments")
