from flask import Flask, request, jsonify, g, abort, make_response

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    req_json = request.get_json(force=True, silent=True)
    if req_json is None:
        req_json = {}
    return jsonify(code=0,
                   message='',
                   data=req_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
