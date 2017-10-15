#!notify/bin/python3

import os
import sys
from pushbullet import Pushbullet

if len(sys.argv) >= 3:
    api_key = os.environ["PB_API_KEY"]
    pb = Pushbullet(api_key)
    title = sys.argv[1]
    body = sys.argv[2]
    
    pb.push_note(title, body)
else:
    print("Error: Missing arguments")
