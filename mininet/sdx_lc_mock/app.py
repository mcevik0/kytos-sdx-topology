""" sdx_lc mock test """

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/SDX-LC/1.0.0/topology', methods=['POST'])
def receive_topology():
    """ listen for sdx topology """
    try:
        data = request.json
    except BadRequest:
        result = "The request body is not a well-formed JSON."
        print("%s %s", result, 400)
        raise BadRequest(result) from BadRequest
    return jsonify(data)


if __name__ == '__main__':
    app.run()
