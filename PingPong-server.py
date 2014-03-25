from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    print(request.get_json())
    return request.get_json()

if __name__ == '__main__':
    app.run()
