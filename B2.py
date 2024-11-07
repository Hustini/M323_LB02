from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B2G', methods=['GET'])
def funktion():
    def add(x, y):
        return x + y
    tmp = add
    result = tmp(2, 3)
    return jsonify({
        'approach': 'store func in variable',
        'result': result
    })


@app.route('/B2F', methods=['GET'])
def get_immutable_values_result():
    return jsonify({
        'approach': 'functional algorithm',
        'result': result,
        'numbers': numbers
    })


@app.route('/B2E', methods=['GET'])
def get_functional_sum():
    return jsonify({})


if __name__ == '__main__':
    app.run()
