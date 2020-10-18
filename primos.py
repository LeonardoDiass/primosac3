import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def primos():
    primos = []
    for i in range(1, 101):
        x = 2
        while x < i:
            if i % x == 0:
                break
            x += 1
        if x == i:
            primos.append(i)
    return str(primos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
