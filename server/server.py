from flask import Flask, request, jsonify, g, abort, make_response

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    return jsonify(code=0,
                   message='',
                   data=[])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
