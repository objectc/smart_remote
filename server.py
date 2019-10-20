import logging
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import abort, jsonify

from flask import Flask

app = Flask(__name__)
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

COMMANDS = {
    'POWER': 'POWER',
    'COOL': 'COOL',
    'SPEED_UP': 'SPEED_UP',
    'SPEED_DOWN': 'SPEED_DOWN',
    'TEMP_UP': 'TEMP_UP',
    'TEMP_DOWN': 'TEMP_DOWN',
    'TIMER': 'TIMER',
    'ROTATE': 'ROTATE',
    'NARROW': 'NARROW',
    'WIDE': 'WIDE'
}


@app.route("/dyson", methods=['GET'])
def getDyson():
    command = request.args.get('command')
    command = command.lower()
    if command:
        if command in COMMANDS.keys():
            command_str = 'irsend send_once Dyson ' + COMMANDS[command]
            os.system(command_str)
            resData = {'msg': 'success'}
            response = jsonify(resData)
            return response
    return jsonify({'msg': 'no commands found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
