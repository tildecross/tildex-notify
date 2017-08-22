#!notify/bin/python3

import os
import sys
from pushbullet import Pushbullet

if len(sys.argv) >= 3:
    api_key = os.environ["PB_API_KEY"]
    pb = Pushbullet(api_key)

    pb.push_note(sys.argv[1], sys.argv[2])
else:
    print("Error: Missing arguments")
