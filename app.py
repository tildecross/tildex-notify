#!notify/bin/python3

import hug
import os
from pushbullet import Pushbullet


@hug.cli()
def create_note(title: hug.types.text, content: hug.types.text):
    api_key = os.environ["PB_API_KEY"]
    pb = Pushbullet(api_key)
    pb.push_note(title, content)


if __name__ == '__main__':
    create_note.interface.cli()
