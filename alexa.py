import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

COMMANDS = {
            'power': 'POWER', 
            'cool': 'COOL', 
            'speed up': 'SPEED_UP', 
            'speed down':'SPEED_DOWN', 
            'temperature up': 'TEMP_UP',
            'temperature down': 'TEMP_DOWN', 
            'timer': 'TIMER', 
            'rotate': 'ROTATE', 
            'narrow':'NARROW', 
            'wide':'WIDE'
            }

@ask.launch
def launch():
    pass


@ask.intent('RemoteIntent', mapping = {'command': 'command'})
def remote(command, room):
    if command in COMMANDS.keys():
        command_str = 'irsend send_once Dyson ' + COMMANDS[command]
        os.system(command_str)
        return statement('dyson '+command)
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
