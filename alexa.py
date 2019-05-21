import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

COMMANDS = {
            'POWER': 'power', 
            'COOL': 'cool', 
            'SPEED_UP': 'speed up', 
            'SPEED_DOWN': 'speed down', 
            'TEMP_UP': 'temperature up',
            'TEMP_DOWN': 'temperature down', 
            'TIMER': 'timer', 
            'ROTATE': 'rotate', 
            'NARROW': 'narrow', 
            'WIDE': 'wide'
            }

@ask.launch
def launch():
    pass


@ask.intent('RemoteIntent', mapping = {'command': 'command'})
def remote(command, room):
    if command in COMMANDS.values():
        command_str = 'irsend send_once Dyson' + command
        os.system(command_str)
        return statement('dyson'+command)
    else:
        return statement('no command'+command)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
