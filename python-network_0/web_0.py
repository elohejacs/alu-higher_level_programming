from flask import Flask
app = Flask(__name__)

@app.route('/route_5', methods=['GET'])
def route_5():
    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
