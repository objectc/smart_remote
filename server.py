import logging
import os
from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS
from flask import abort, jsonify

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

COMMANDS = {
    'power': 'POWER',
    'cool': 'COOL',
            'speed up': 'SPEED_UP',
            'speed down': 'SPEED_DOWN',
            'temperature up': 'TEMP_UP',
            'temperature down': 'TEMP_DOWN',
            'timer': 'TIMER',
            'rotate': 'ROTATE',
            'narrow': 'NARROW',
            'wide': 'WIDE'
}


@app.route("/dyson", methods=['GET'])
def getDyson():
    command = request.args.get('command')
    if command:
        if command in COMMANDS.keys():
            command_str = 'irsend send_once Dyson ' + COMMANDS[command]
            os.system(command_str)
            resData = {'status': 'success'}
            response = jsonify(resData)
            return response


if __name__ == '__main__':
    app.run(debug=True)
